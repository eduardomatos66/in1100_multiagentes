#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc2 import Race
from sc2.ids.unit_typeid import UnitTypeId

from core.bot.generic.generic_bot_player import GenericBotPlayer
from strategy.managers.gather_manager import GatherBotManager
from strategy.managers.trainer_manager import TrainerBotManager


class MyBotPlayer(GenericBotPlayer):
    """ The player class of the game match """

    def __init__(self):
        super(MyBotPlayer, self).__init__(race_type=Race.Terran)

    def on_start(self):
        """ Allows initializing the bot when the game data is available """
        self.add_bot(GatherBotManager(bot_player=self))
        self.add_bot(TrainerBotManager(bot_player=self))
        # self.add_bot(ScoutBotManager(bot_player=self))
        # self.add_bot(BuildBotManager(bot_player=self))

    def get_units_by_type(self, types):
        """
        :param list[UnitTypeId] types:
        :return list[sc2.unit.Unit]:
        """
        return [unit for unit in self.units if unit.type_id in types]

    def get_units_by_position(self, position_x, position_y):
        """
        :param float position_x:
        :param float position_y:
        :return sc2.unit.Unit:
        """
        for unit in self.units:
            if [unit.position.x, unit.position.y] == [position_x, position_y]:
                return unit

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        self.sync_bot_requests()
        await self.trigger_bots_default_behavior(iteration)

    def sync_bot_requests(self):
        """ Update the requests for each bot added """
        for bot in self.bots.values():
            bot.sync_requests()

    async def trigger_bots_default_behavior(self, iteration):
        """
        :param int iteration:
        """
        for bot in self.bots.values():
            await bot.default_behavior(iteration=iteration)
