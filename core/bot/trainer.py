#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gather bot unit
"""
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_unit_creator import GenericBotUnitCreator


class Trainer(GenericBotUnitCreator):
    """  A Gather bot unit class """

    should_train_scv = False

    def __init__(self, bot_player, bot_manager, request, unit_tags):
        """
        :param core.bot.generic.generic_bot_player.GenericBotPlayer bot_player:
        :param core.bot.generic.generic_bot_manager.GenericBotManager bot_manager:
        :param core.register_board.request.Request request:
        :param list[int] unit_tags:
        """
        super(Trainer, self).__init__(bot_player, bot_manager, request, unit_tags)
        self._train_scv_allowed = True
        self._goal_max_trainer = []

    def set_default_max_trainer(self, goal_max_trainer):
        """
        Get default max trainer
        """
        self._goal_max_trainer = goal_max_trainer

    async def default_behavior(self, iteration):
        """
        The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        # Do 60 in 60 iteration checks
        for unit_id, max_value in self._goal_max_trainer:
            pass
        # if not iteration % 40:
        #     await self.check_need_scv_training()

    async def check_need_scv_training(self):
        """
        Check need of train SCVs
        """
        if self.should_train_scv:
            await self.train_scv()

    async def toggle_train_scv(self, should_train):
        """
        Toggle train SCV
        :param boolean should_train:
        """
        self.should_train_scv = should_train

    async def train_scv(self):
        """
        Train SCV
        """
        num_workers = len(self.bot_player.workers)
        num_idle_workers = len(self.bot_player.workers.idle)
        command_centers = self.bot_player.units(UnitTypeId.COMMANDCENTER).ready

        for cmd_cen in command_centers:
            if self.bot_player.can_afford(UnitTypeId.SCV) and cmd_cen.noqueue:
                refinery_slots = 0
                refs = self.bot_player.units(UnitTypeId.REFINERY).ready.closer_than(20, cmd_cen.position)
                for ref in refs:
                    refinery_slots += ref.ideal_harvesters - ref.assigned_harvesters

                if num_workers == 0 \
                        or cmd_cen.assigned_harvesters < (cmd_cen.ideal_harvesters + refinery_slots - num_idle_workers):

                    # Need to train SCV
                    await self.bot_player.do(cmd_cen.train(UnitTypeId.SCV))
