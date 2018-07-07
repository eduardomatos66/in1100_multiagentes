#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class InfoType(Enum):
    """
    Info type
    """
    ENEMY_POSITION = 'ENEMY_POSITION'
    ENEMY_NEARBY = 'ENEMY_NEARBY'
