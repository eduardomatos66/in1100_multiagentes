#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class RequestPriority(Enum):
    """
    Request Priority
    """
    PRIORITY_HIGHER = 0
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3
    PRIORITY_LOWER = 4

    def get_next(self):
        """
        Get next higher priority level.
        :return core.communication.constant.RequestPriority:
        """
        if self.value == RequestPriority.PRIORITY_HIGH.value:
            return RequestPriority.PRIORITY_HIGHER
        elif self.value == RequestPriority.PRIORITY_MEDIUM.value:
            return RequestPriority.PRIORITY_HIGH
        elif self.value == RequestPriority.PRIORITY_LOW.value:
            return RequestPriority.PRIORITY_MEDIUM
        elif self.value == RequestPriority.PRIORITY_LOWER.value:
            return RequestPriority.PRIORITY_LOW
