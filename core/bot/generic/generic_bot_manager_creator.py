#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" GenericBotUnitCreator """
from core.bot.generic.generic_bot_manager import GenericBotManager
from core.bot.terran.race_dependencies import dependencies_constants
from core.bot.terran.race_dependencies.building_dependencies import building_dependencies_dict
from core.bot.terran.race_dependencies.training_dependencies import training_dependencies_dict

BUILD = 'build'
TRAIN = 'train'


class GenericBotManagerCreator(GenericBotManager):
    """ Generic bot non-player unit class, which represents a sc2.unit.Unit on the game """

    def __init__(self, bot_player):
        """
        :param core.bot.generic.generic_bot_player.GenericBotPlayer bot_player:
        """
        super(GenericBotManagerCreator, self).__init__(bot_player)
        self.dict_dependencies = self._set_dependencies()

    def find_request(self):
        """ Implements the logic to find the requests that should be handled by the bot
        :return list[core.register_board.request.Request]
        """
        raise NotImplementedError

    async def requests_handler(self, iteration):
        """ Logic to go through the bot requests
        :param int iteration: Game loop iteration
        """
        raise NotImplementedError

    def requests_status_update(self):
        """ Logic to update the requests status """
        raise NotImplementedError

    def _set_dependencies(self):
        """
        Set creation dependencies according to bot manager
        :return dict:
        """
        result = None
        if TRAIN in str.lower(self.__class__.__name__):
            result = training_dependencies_dict
        elif BUILD in str.lower(self.__class__.__name__):
            result = building_dependencies_dict
        return result

    async def check_dependencies(self, requested_unit_type_id):
        """
        Check request dependencies.
        :param  sc2.ids.unit_typeid.UnitTypeId requested_unit_type_id:
        :return bool:
        """
        request_dependencies = self.dict_dependencies.get(requested_unit_type_id)

        can_build = self.bot_player.can_afford(requested_unit_type_id)
        can_build = can_build.can_afford_minerals and can_build.can_afford_vespene

        if request_dependencies:
            build_dependencies = request_dependencies[dependencies_constants.BUILD]
            can_build = can_build and await self.check_build_dependencies(build_dependencies, can_build)

            tech_dependencies = request_dependencies[dependencies_constants.TECHNOLOGY]
            can_build = can_build and await self.check_technology_dependencies(tech_dependencies, can_build)

            supply_dependencies = request_dependencies[dependencies_constants.SUPPLY]
            can_build = can_build and await self.check_supply_dependencies(supply_dependencies, can_build)

        # TODO: modify return with existent dependencies
        return can_build

    async def check_supply_dependencies(self, supply_dependencies, can_build):
        """
        Check supply dependencies
        :param supply_dependencies:
        :param can_build:
        :return:
        """
        if self.bot_player.supply_left > supply_dependencies:
            pass
        else:
            can_build = False
        return can_build

    async def check_technology_dependencies(self, tech_dependencies, can_build):
        """
        Check technology dependencies
        :param tech_dependencies:
        :param can_build:
        :return:
        """
        for dependency in tech_dependencies:
            if self.bot_player.get_available_abilities(dependency).amount > 0:
                can_build = can_build and True
            else:
                can_build = False
                break
        return can_build

    async def check_build_dependencies(self, build_dependencies, can_build):
        """
        Check build dependencies
        :param build_dependencies:
        :param can_build:
        :return:
        """
        for dependency in build_dependencies:
            if self.bot_player.units(dependency).amount > 0:
                can_build = can_build and True
            else:
                can_build = False
                break
        return can_build

    async def default_behavior(self, iteration):
        """ The default behavior of the bot
        :param int iteration: Game loop iteration
        """
        raise NotImplementedError
