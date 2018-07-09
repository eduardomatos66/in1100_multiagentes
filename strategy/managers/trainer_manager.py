#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" TrainerBotManager """
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_manager_creator import GenericBotManagerCreator
from core.bot.terran.race_dependencies import dependencies_constants
from core.bot.trainer import Trainer
from core.communication.constants.operation_type_id import OperationTypeId


class TrainerBotManager(GenericBotManagerCreator):
    """ Build manager class """

    processed_requests = []

    def __init__(self, bot_player):
        """
        :param core.bot.generic_bot_player.GenericBotPlayer bot_player:
        """
        super(TrainerBotManager, self).__init__(bot_player)
        self.trainer_unit = Trainer(bot_player, self, None, [])

        self._goal_max_trainer = [
            (UnitTypeId.SCV, 26),
            (UnitTypeId.MARINE, 10),
            (UnitTypeId.MARAUDER, 10),
            (UnitTypeId.LIBERATOR, 4),
            (UnitTypeId.SIEGETANK, 10)
        ]

    async def default_behavior(self, iteration):
        """
        Trainer default behavior
        :param int iteration:
        """
        if iteration % 40 == 0:
            for unit_type_id, max_value in self._goal_max_trainer:
                await self.train_by_checking_needs(unit_type_id, max_value)

    def set_default_max_trainer(self, goal_max_trainer):
        """
        Get default max trainer
        """
        # TODO Use this to set default training goal
        self._goal_max_trainer = goal_max_trainer

    def find_request(self):
        """ Implements the logic to find the requests that should be handled by the bot
        :return list[core.register_board.request.Request]
        """
        return self.bot_player.board_request.search_request_by_operation_ids(
            [OperationTypeId.TRAIN_BASIC_UNIT_ALLOW,
             OperationTypeId.TRAIN_BASIC_UNIT_DENY,
             OperationTypeId.TRAIN]
        )

    def requests_status_update(self):
        """ Logic to update the requests status """
        for request in self.processed_requests:
            self.bot_player.board_request.remove(request)

        self.processed_requests.clear()

    async def requests_handler(self, iteration):
        """
        Logic to go through the bot requests
        :param int iteration: Game loop iteration
        """
        for request in self.requests:
            await self.train_by_checking_needs(request.unit_type_id, request.amount, request.location)

    async def train_by_checking_needs(self, unit_type_id, amount, location=None):
        """
        Train by checking needs
        :param sc2.ids.unit_typeid.UnitTypeId unit_type_id:
        :param int amount:
        :param sc2.position.Point2 location:
        """
        dependencies = await self.check_dependencies(unit_type_id)
        if len(self.bot_player.units(unit_type_id)) < amount and dependencies:

            unit_trainer = await self._get_best_unit_trainer(unit_type_id, location)
            if unit_trainer:
                await self.trainer_unit.train_unit(unit_trainer, unit_type_id, amount)
            else:
                # TODO Raise and exception or print unit_trainer is None or request build construction
                pass

        elif dependencies:
            # TODO Request build construction
            pass

    async def _get_best_unit_trainer(self, unit_type_id, location=None):
        """
        Get best unit trainer build
        :param sc2.ids.unit_typeid.UnitTypeId unit_type_id:
        :param sc2.position.Point2 location:
        :return sc2.ids.unit_typeid.UnitTypeId:
        """
        result = None
        request_dependencies = self.dict_dependencies.get(unit_type_id)
        build_dependencies = request_dependencies[dependencies_constants.BUILD]

        possible_constructions = self.bot_player.units(build_dependencies[0])
        if possible_constructions:
            result = possible_constructions[0]

        # TODO get best location to train

        return result
