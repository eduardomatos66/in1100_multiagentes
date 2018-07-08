#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc2.ids.unit_typeid import UnitTypeId
from core.bot.dependencies_constants import BUILD, TECHNOLOGY, SUPPLY

building_dependencies_dict = {
    UnitTypeId.SUPPLYDEPOT: {
        BUILD: [],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.REFINERY: {
        BUILD: [],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.BARRACKS: {
        BUILD: [UnitTypeId.COMMANDCENTER],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.BARRACKSTECHLAB: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.ENGINEERINGBAY: {
        BUILD: [UnitTypeId.COMMANDCENTER],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.BUNKER: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.MISSILETURRET: {
        BUILD: [UnitTypeId.ENGINEERINGBAY],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.FACTORY: {
        BUILD: [UnitTypeId.BARRACKS],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.FACTORYTECHLAB: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.ARMORY: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.STARPORT: {
        BUILD: [UnitTypeId.FACTORY],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.STARPORTTECHLAB: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 0
    },
    UnitTypeId.SCIENCEFACILITY: {
        BUILD: [UnitTypeId.STARPORT],
        TECHNOLOGY: [],
        SUPPLY: 0
    }
}
