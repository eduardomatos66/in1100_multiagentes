#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc2.ids.unit_typeid import UnitTypeId
from core.bot.dependencies_constants import BUILD, TECHNOLOGY, SUPPLY

training_dependencies_dict = {
    UnitTypeId.SCV: {
        BUILD: [UnitTypeId.COMMANDCENTER],
        TECHNOLOGY: [],
        SUPPLY: 1
    },
    UnitTypeId.MARINE: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.MARAUDER: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.REAPER: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 1
    },
    UnitTypeId.GHOST: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.HELLION: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.SIEGETANK: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 3
    },
    UnitTypeId.THOR: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 6
    },
    UnitTypeId.HELLBATACGLUESCREENDUMMY: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.WIDOWMINE: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.CYCLONE: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 3
    },
    UnitTypeId.VIKINGSKY_UNIT: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.MEDIVAC: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.RAVEN: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 2
    },
    UnitTypeId.BANSHEE: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 3
    },
    UnitTypeId.BATTLECRUISER: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 6
    },
    UnitTypeId.LIBERATOR: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 3
    }
}
