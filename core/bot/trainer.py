#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gather bot unit
"""
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_unit import GenericBotUnit


class Trainer(GenericBotUnit):
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

    async def default_behavior(self, iteration):
        """
        The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        pass # Trainer has no default behavior

    async def train_unit(self, unit_trainer, unit_id, max_value):
        """
        Train unit.
        :param unit_trainer:
        :param unit_id:
        :param max_value:
        """
        if max_value > 5:
            max_value = 5

        for i in range(max_value):
            if self.bot_player.can_afford(unit_id):
                await self.bot_player.do(unit_trainer.train(unit_id))

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
