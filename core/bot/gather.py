#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gather bot unit
"""
from sc2.ids.ability_id import AbilityId

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

    async def default_behavior(self, iteration):
        """
        The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        # Do 60 in 60 iteration checks
        if not iteration % 60:
            await self._handle_gather_resources()

    async def _handle_gather_resources(self):
        """
        Handle gather resource
        :return:
        """
        await self._handle_assigned_geysers()
        await self._handle_idle_workers()

        # if self.bot_player.state.mineral_field:
        #     await self.bot_player.distribute_workers()

    async def _handle_assigned_geysers(self):
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

    async def _handle_idle_workers(self):
        """
        Hanle idle workers by putting them back to gathering
        """
        for idle_worker in self.bot_manager.find_available_scvs_units()[:4]:
            if self.bot_player.state.mineral_field:
                mf = self.bot_player.state.mineral_field.closest_to(idle_worker)
                if mf:
                    await self.bot_player.do(idle_worker.gather(mf))
