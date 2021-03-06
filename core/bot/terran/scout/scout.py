#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_unit import GenericBotUnit
from core.bot import util
from core.communication.constants.request_priority import RequestPriority
from core.communication.constants.operation_type_id import OperationTypeId
from core.communication.item.request import RequestStatus, Request


class Scout(GenericBotUnit):
    """  A Scout bot unit class """

    def __init__(self, bot_player, iteration, request, unit_tags):
        """
        :param core.bot.generic_bot_player.GenericBotPlayer bot_player:
        :param int iteration:
        :param core.register_board.request.Request request:
        :param list(int) unit_tags:
        """
        super(Scout, self).__init__(
            bot_player=bot_player, iteration=iteration, request=request, unit_tags=unit_tags
        )

        self.cmd_center = None
        self.current_scout = None
        self.found_enemy_base = False
        self.enemy_start_position = None
        self.enemy_location_counter = 0
        self.mean_location = None
        self.is_enemy_coming = False
        self.current_idle_units = None
        self._last_positions = list()

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        self.log("Executing {}".format(self._info.request))
        self.info.status = RequestStatus.ON_GOING
        await self.scout()

    async def move_scout_to(self, position):
        self.log("Moving Scout")
        unit = self.bot_player.get_current_worker_unit(self._info.unit_tags[0])
        if unit:
            await self.bot_player.do(unit.move(position))
        else:
            self.info.request.status = RequestStatus.FAILED

    def set_scout(self):
        # TODO: We can get the scout using self.get_current_scout().
        # TODO Evaluate to replace this method for this new one
        self.log("Setting Scout")
        if not self.current_scout:
            self.current_scout = self.get_current_scout()
            self.set_mean_location()

    def set_mean_location(self):
        self.mean_location = util.get_mean_location(
            self.bot_player.start_location, self.bot_player.enemy_start_locations[0]
        )

    def set_cmd_center(self):
        self.log("Setting cmd center")
        if self.cmd_center is None:
            self.cmd_center = self.bot_player.units.structure[0]

    def set_enemy_position(self):
        self.log("Found enemy base")
        self.enemy_start_position = self.bot_player.known_enemy_structures[0].position
        # self.bot_player.board_info.register(Info(bot=self, value=self.enemy_start_position, type=InfoType.ENEMY_POSITION))

    async def visit_enemy(self):
        await self.move_scout_to(self.bot_player.enemy_start_locations[self.enemy_location_counter])

    async def patrol(self):
        self.bot_player.board_request.register(
            Request(request_priority=RequestPriority.PRIORITY_HIGHER, unit_type_id=UnitTypeId.SCV,
                    operation_type_id=OperationTypeId.PATROL)
        )
        await self.visit_base()

    async def visit_base(self):
        self.log("Visiting base")
        if self.bot_player.known_enemy_units.not_structure:
            self.register_enemy_units(self.bot_player.known_enemy_units.not_structure)
        await self.move_scout_to(util.add_to_location(self.cmd_center.position, randint(-9 ,9)))

    async def visit_middle(self):
        self.log("Visiting middle")
        # If found enemies before moving, store it on the board
        if self.bot_player.known_enemy_units.not_structure:
            self.register_enemy_units(self.bot_player.known_enemy_units.not_structure)
        await self.move_scout_to(util.add_to_location(util.get_mean_location(
            self.bot_player.start_location, self.bot_player.enemy_start_locations[0]
        ), randint(-9, 9)))

    # def register_enemy_units(self, enemy_units):
        # self.bot_player.board_info.register(
        #     Info(bot=self, value=len(enemy_units), type=InfoType.ENEMY_NEARBY, location=enemy_units[0].position))

    def is_enemy_structure_nearby(self):
        if self.bot_player.known_enemy_structures:
            self.set_enemy_position()
            return True

    def is_enemy_units_nearby(self):
        if self.bot_player.known_enemy_structures:
            self.set_enemy_position()
            return True

    async def scout(self):
        self.set_cmd_center()
        await self.visit_enemy()
