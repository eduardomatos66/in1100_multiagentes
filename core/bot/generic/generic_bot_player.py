#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc2 import player

from core.bot.generic.generic_bot import GenericBot
from core.bot.generic.generic_bot_manager import GenericBotManager
from core.exceptions import NotAddingNonPlayerBotException
from core.communication.board.request_board import RequestBoard


class GenericBotPlayer(GenericBot):
    """ Generic bot player class, which can observer and operate the environment """

    def __init__(self, race_type):
        """
        :param sc2.data.Race race_type:
        """
        super(GenericBotPlayer, self).__init__(race_type)
        self._bots = dict()
        self._board_request = RequestBoard()

    @property
    def bots(self):
        """
        :return dict:
        """
        return self._bots

    @property
    def board_request(self):
        """
        :return core.register_board.boards.BoardRequest:
        """
        return self._board_request

    def send_request(self, request):
        """
        :param core.register_board.request.Request request:
        """
        self._board_request.register(request)

    def add_bot(self, bot):
        """
        :param core.bot.generic_bot_manager.GenericBotManager bot:
        :raise NotAddingNonPlayerBot:
        """
        if not isinstance(bot, GenericBotManager):
            raise NotAddingNonPlayerBotException()

        self._bots[str(bot)] = bot

    def build_bot_player(self):
        """
        :return sc2.player.Bot
        """
        return player.Bot(race=self._race_type, ai=self)

    def get_current_worker_unit(self, unit_tag):
        """ Get worker unit
        :param int unit_tag:
        :return sc2.unit.Unit:
        """
        for worker in self.workers:
            if worker.tag == unit_tag:
                return worker

    def get_current_units(self, unit_tags):
        """ Get current group of unit
        :param list(int) unit_tags:
        :return list(sc2.unit.Unit):
        """
        result = list()
        for unit in self.units:
            if unit.tag in unit_tags:
                result.append(unit)
        return result

    def get_owned_expansions_locations(self):
        """ Get the Point2 (location) of current expansion
        :return list[sc2.position.Point2]:
        """
        return list(self.owned_expansions.keys())

    def get_resources_locations(self, expansion_location):
        """ Get all the Minerals and Vespene Geysers positions around our expansion
        :param sc2.position.Point2 expansion_location:
        :return list[sc2.unit.Unit]:
        """
        return list(self.expansion_locations.get(expansion_location))

    def on_start(self):
        """ Allows initializing the bot when the game data is available """
        raise NotImplementedError

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        raise NotImplementedError
