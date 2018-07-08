#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.dependencies_constants import BUILD, TECHNOLOGY, SUPPLY
from core.bot.generic.generic_bot_unit import GenericBotUnit
from core.bot.terran.build.build_dependencies import building_dependencies_dict
from core.bot.training_dependencies import training_dependencies_dict
from core.communication.constants.operation_type_id import OperationTypeId
from core.communication.item.request import Request
from strategy.cin_deem_team.terran.managers.builder_manager import BuildBotManager
from strategy.managers.trainer_manager import TrainerBotManager


class GenericBotUnitCreator(GenericBotUnit):
    """ Generic bot non-player unit class, which represents a sc2.unit.Unit on the game """

    def __init__(self, bot_player, bot_manager, request, unit_tags):
        """
        :param core.bot.generic.generic_bot_player.GenericBotPlayer bot_player:
        :param core.bot.generic.generic_bot_manager.GenericBotManager bot_manager:
        :param core.register_board.request.Request request:
        :param list[int] unit_tags:
        """
        super(GenericBotUnitCreator, self).__init__(bot_player, bot_manager, request, unit_tags)
        self.dict_dependencies = self._set_dependencies()

    def _set_dependencies(self):
        """
        Set creation dependencies according to bot manager
        :return dict:
        """
        result = None
        if isinstance(self.bot_manager, TrainerBotManager):
            result = training_dependencies_dict
        elif isinstance(self.bot_manager, BuildBotManager):
            result = building_dependencies_dict
        return result

    async def _check_dependencies(self, request):
        """
        Check request dependencies.
        :param core.register_board.request.Request request:
        :return bool:
        """
        requested_unit = request.unit_type_id
        request_dependencies = self.dict_dependencies.get(requested_unit)

        can_build = self.bot_player.can_afford(requested_unit)
        can_build = can_build.can_afford_minerals and can_build.can_afford_vespene

        if request_dependencies:
            build_dependencies = request_dependencies[BUILD]
            can_build = can_build and await self.check_build_dependencies(request, build_dependencies, can_build)

            tech_dependencies = request_dependencies[TECHNOLOGY]
            can_build = can_build and await self.check_technology_dependencies(request, tech_dependencies, can_build)

            supply_dependencies = request_dependencies[SUPPLY]
            can_build = can_build and await self.check_supply_dependencies(request, supply_dependencies, can_build)

        return can_build

    async def check_supply_dependencies(self, request, supply_dependencies, can_build):
        """
        Check supply dependencies
        :param core.register_board.request.Request request:
        :param supply_dependencies:
        :param can_build:
        :return:
        """
        if self.bot_player.supply_left > supply_dependencies:
            pass
        else:
            self.bot_player.board_request.register(
                Request(request_priority=request.request_priority_level, unit_type_id=UnitTypeId.SUPPLYDEPOT,
                        operation_type_id=OperationTypeId.BUILD)
            )
            can_build = False
        return can_build

    async def check_technology_dependencies(self, request, tech_dependencies, can_build):
        """
        Check technology dependencies
        :param core.register_board.request.Request request:
        :param tech_dependencies:
        :param can_build:
        :return:
        """
        for dependency in tech_dependencies:
            if self.bot_player.get_available_abilities(dependency).amount > 0:
                can_build = can_build and True
            else:
                self.bot_player.board_request.register(
                    Request(request_priority=request.request_priority_level, unit_type_id=dependency,
                            operation_type_id=OperationTypeId.RESEARCH_TECHNOLOGY)
                )
                can_build = False
                break
        return can_build

    async def check_build_dependencies(self, request, build_dependencies, can_build):
        """
        Check build dependencies
        :param core.register_board.request.Request request:
        :param build_dependencies:
        :param can_build:
        :return:
        """
        for dependency in build_dependencies:
            if self.bot_player.units(dependency).amount > 0:
                can_build = can_build and True
            else:
                self.bot_player.board_request.register(
                    Request(request_priority=request.request_priority_level, unit_type_id=dependency,
                            operation_type_id=OperationTypeId.BUILD)
                )
                can_build = False
                break
        return can_build

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        raise NotImplementedError
