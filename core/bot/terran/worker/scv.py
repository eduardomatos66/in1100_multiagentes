#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Default SCV bot class
"""

from core.bot.terran.generic_terran_bot import GenericTerranBot
from core.behavior.terran.worker import logic


class SCV(GenericTerranBot):
    """ A default SCV bot class """

    def on_start(self):
        """ Allows initializing the bot when the game data is available """
        pass

    async def default_on_step(self, iteration, observer):
        """ Ran on every game step (looped in real-time mode).
        :param int iteration: Game loop iteration
        :param core.bot.generic_bot.GenericBot observer: The supreme observer
        """
        await logic.scv_logic(self, iteration, observer)
