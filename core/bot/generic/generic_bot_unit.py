#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.bot.generic.generic_bot import GenericBot


class GenericBotUnit(GenericBot):
    """ Generic bot non-player unit class, which represents a sc2.unit.Unit on the game """

    def __init__(self, bot_player, bot_manager, request, unit_tags):
        """
        :param core.bot.generic.generic_bot_player.GenericBotPlayer bot_player:
        :param core.bot.generic.generic_bot_manager.GenericBotManager bot_manager:
        :param core.register_board.request.Request request:
        :param list[int] unit_tags:
        """
        super(GenericBotUnit, self).__init__(bot_player)
        self._bot_player = bot_player
        self._bot_manager = bot_manager
        self._unit_tags = unit_tags
        self._request = request

    @property
    def bot_player(self):
        """
        :return core.bot.generic_bot_player.GenericBotPlayer:
        """
        return self._bot_player

    @property
    def bot_manager(self):
        """
        :return core.bot.generic.generic_bot_manager.GenericBotManager:
        """
        return self._bot_manager

    @property
    def request(self):
        """
        :return core.register_board.request.Request:
        """
        return self._request

    def set_request(self, request):
        """
        :param core.register_board.request.Request request:
        """
        self._request = request

    @property
    def unit_tags(self):
        """
        :return int:
        """
        return self._unit_tags

    def is_idle(self):
        """
        :return bool:
        """
        unit = self.bot_player.get_current_worker_unit(self._request.unit_tags)
        if unit:
            return unit.is_idle
        else:
            return False

    def are_idle(self):
        """
        :return bool:
        """
        result = True
        units = self.bot_player.get_current_units(self._request.unit_tags)
        if units:
            for unit in units:
                if not unit.is_idle:
                    result = False
        else:
            result = False
        return result

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        raise NotImplementedError
