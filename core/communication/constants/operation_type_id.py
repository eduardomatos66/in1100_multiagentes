#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Operation Type Id """

from enum import Enum


class OperationTypeId(Enum):
    """
    Operation Type Id
    """
    ATTACK = 'ATTACK'

    BUILD = 'BUILD'

    DEFEND = 'DEFEND'

    GATHER_MINERALS = 'GATHER_MINERALS'
    GATHER_VESPENE = 'GATHER_VESPENE'

    PATROL = 'PATROL'

    RESEARCH_TECHNOLOGY = 'RESEARCH_TECHNOLOGY'

    SCOUT = 'SCOUT'

    TRAIN_BASIC_UNIT_ALLOW = 'ALLOW SCV'
    TRAIN_BASIC_UNIT_DENY = 'DENY SCV'
    TRAIN = "TRAIN"

    WARN = 'WARN'
