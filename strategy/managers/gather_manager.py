#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.bot.generic.generic_bot_manager import GenericBotManager
from core.bot.gather import Gather
from core.communication.constants.operation_type_id import OperationTypeId


class GatherBotManager(GenericBotManager):
    """ Build manager class """

    processed_requests = []

    def __init__(self, bot_player):
        """
        :param core.bot.generic_bot_player.GenericBotPlayer bot_player:
        """
        super(GatherBotManager, self).__init__(bot_player)
        self.gather_unit = Gather(bot_player, self, None, [])

    def find_request(self):
        """ Implements the logic to find the requests that should be handled by the bot
        :return list[core.register_board.request.Request]
        """
        return self.bot_player.board_request.search_request_by_operation_ids([OperationTypeId.GATHER_MINERALS,
                                                                              OperationTypeId.GATHER_VESPENE])

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
            pass
        else:
            await self.update_gather(iteration)

    async def update_gather(self, iteration):
        """
        :param int iteration: Game loop iteration
        """
        if iteration > 0:
            await self.gather_unit.default_behavior(iteration)
