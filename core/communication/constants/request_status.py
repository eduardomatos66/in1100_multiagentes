#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class RequestStatus(Enum):
    """
    Request Status
    """
    TO_BE_DONE = "TO BE DONE"
    ON_GOING = "ON GOING"
    DONE = "DONE"
    DISMISSED = "DISMISSED"
    FAILED = "FAILED"
