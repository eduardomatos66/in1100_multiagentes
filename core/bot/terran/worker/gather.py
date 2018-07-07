#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_manager import GenericBotManager


def get_workers_free_slots(unit):
    return unit.ideal_harvesters - unit.assigned_harvesters


def scv_can_gather(scv):
    orders = scv.orders
    return len(orders) < 1 or orders[0].ability.id in [AbilityId.HARVEST_GATHER, AbilityId.HARVEST_RETURN]


class Gather(GenericBotManager):
    """  A Gather bot class """

    should_train_scv = False

    def __init__(self, bot_player):
        """
        :param core.bot.generic_bot_player.GenericBotPlayer bot_player:
        """
        super(Gather, self).__init__(bot_player)
        self._info = None

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
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

    async def toggle_train_scv(self, should_train):
        self.should_train_scv = should_train

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
                if self.find_available_scvs_units(is_idle=False):
                    w = self.find_available_scvs_units(is_idle=False)[0]
                    if len(w.orders) == 1 and w.orders[0].ability.id in [AbilityId.HARVEST_RETURN]:
                        await self.bot_player.do(w.move(g))
                        await self.bot_player.do(w.return_resource(queue=True))
                    else:
                        await self.bot_player.do(w.gather(g))

    async def handle_idle_workers(self):
        """
        Hanle idle workers by putting them back to gathering
        """
        for idle_worker in self.find_available_scvs_units()[:4]:
            if self.bot_player.state.mineral_field:
                mf = self.bot_player.state.mineral_field.closest_to(idle_worker)
                if mf:
                    await self.bot_player.do(idle_worker.gather(mf))

    async def train_scv(self):
        num_workers = len(self.bot_player.workers)
        num_idle_workers = len(self.bot_player.workers.idle)
        command_centers = self.bot_player.units(UnitTypeId.COMMANDCENTER).ready

        for cmd_cen in command_centers:
            if self.bot_player.can_afford(UnitTypeId.SCV) and cmd_cen.noqueue:
                refinery_slots = 0
                refs = self.bot_player.units(UnitTypeId.REFINERY).ready.closer_than(20, cmd_cen.position)
                for ref in refs:
                    refinery_slots += ref.ideal_harvesters - ref.assigned_harvesters

                if num_workers == 0 or cmd_cen.assigned_harvesters < (cmd_cen.ideal_harvesters + refinery_slots - num_idle_workers):
                    #precisa treinar um SCV
                    await self.bot_player.do(cmd_cen.train(UnitTypeId.SCV))
