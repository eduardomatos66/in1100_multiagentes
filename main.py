#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Entry point """

from sc2 import Race
from sc2 import Difficulty
from sc2 import run_game
from sc2 import maps as sc2_maps
from sc2.player import Computer
from sc2.player import Human

from config import maps
from strategy.terran.my_bot_player import MyBotPlayer


if __name__ == '__main__':
    players = [
        MyBotPlayer().build_bot_player(),
        MyBotPlayer().build_bot_player()
        # Human(Race.Terran)
        # Computer(Race.Zerg, Difficulty.VeryEasy)
    ]

    run_game(
        map_settings=sc2_maps.get(maps.MAP_SIMPLE64),
        players=players,
        realtime=False
    )
