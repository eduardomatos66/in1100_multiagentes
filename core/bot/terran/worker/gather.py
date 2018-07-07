#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gather bot unit
"""
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_unit import GenericBotUnit


class Gather(GenericBotUnit):
    """  A Gather bot unit class """

    should_train_scv = False

    def __init__(self, bot_player, bot_manager, request, unit_tags):
        """
        :param core.bot.generic.generic_bot_player.GenericBotPlayer bot_player:
        :param core.bot.generic.generic_bot_manager.GenericBotManager bot_manager:
        :param core.register_board.request.Request request:
        :param list[int] unit_tags:
        """
        super(Gather, self).__init__(bot_player, bot_manager, request, unit_tags)
        self._info = None

    async def default_behavior(self, iteration):
        """
        The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        # Do 60 in 60 iteration checks
        if not iteration % 60:
            await self.gather_resources()
            await self.check_need_scv_training()

    async def check_need_scv_training(self):
        """
        Check need of train SCVs
        """
        if self.should_train_scv:
            await self.train_scv()

    async def gather_resources(self):
        """
        Gather resource
        :return:
        """
        await self.handle_assigned_geysers()

        await self.handle_idle_workers()

        # if self.bot_player.state.mineral_field:
        #     await self.bot_player.distribute_workers()

    async def handle_assigned_geysers(self):
        """
        Hanle assigned harvesters geysers with less than ideal amount.
        """
        for g in self.bot_player.geysers:
            actual = g.assigned_harvesters
            ideal = g.ideal_harvesters
            deficit = ideal - actual

            for x in range(0, deficit):
                if self.bot_manager.find_available_scvs_units(is_idle=False):
                    w = self.bot_manager.find_available_scvs_units(is_idle=False)[0]
                    if len(w.orders) == 1 and w.orders[0].ability.id in [AbilityId.HARVEST_RETURN]:
                        await self.bot_player.do(w.move(g))
                        await self.bot_player.do(w.return_resource(queue=True))
                    else:
                        await self.bot_player.do(w.gather(g))

    async def handle_idle_workers(self):
        """
        Hanle idle workers by putting them back to gathering
        """
        for idle_worker in self.bot_manager.find_available_scvs_units()[:4]:
            if self.bot_player.state.mineral_field:
                mf = self.bot_player.state.mineral_field.closest_to(idle_worker)
                if mf:
                    await self.bot_player.do(idle_worker.gather(mf))

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
