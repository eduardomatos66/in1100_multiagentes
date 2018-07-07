#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class OperationTypeId(Enum):
    """
    Operation Type Id
    """
    ATTACK = 'ATTACK'
    ARMY = 'ARMY'
    BUILD = 'BUILD'
    DEFEND = 'DEFEND'
    PATROL = 'PATROL'
    RESEARCH_TECHNOLOGY = 'RESEARCH_TECHNOLOGY'
    SCOUT = 'SCOUT'
    TRAIN_SCV_ALLOW = 'ALLOW SCV'
    TRAIN_SCV_DENY = 'DENY SCV'
    TRAIN_MARINE_ALLOW = 'ALLOW MARINE'
    TRAIN_MARINE_DENY = 'DENY MARINE'
    WARN = 'WARN'
