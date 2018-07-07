#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.communication.constants.request_status import RequestStatus
from core.communication.item.communication_item import CommunicationItem


class Info(CommunicationItem):
    """ Request information status """

    def __init__(self, item_id, iteration, operation_type_id=None, request_priority=None, location=None,
                 unit_type_id=None, unit_tags=None, amount=0):
        """
        :param int iteration:
        :param core.bot.generic_bot.GenericBot bot:
        :param core.register_board.request.Request request:
        :param list(int) unit_tags:
        """
        super(Info, self).__init__(item_id=item_id, iteration=iteration)

        self._iteration = iteration
        self._bot = 0 # bot
        self._request = 0 # request
        self._status = RequestStatus.TO_BE_DONE
        self._unit_tags = unit_tags
        self._type = type
        self._value = 0 # value
        self._location = location

    @property
    def iteration(self):
        """
        :return int:
        """
        return self._iteration

    @property
    def bot(self):
        """
        :return core.bot.generic_bot.GenericBot:
        """
        return self._bot

    @property
    def request(self):
        """
        :return core.register_board.request.Request:
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        :param core.register_board.request.Request request:
        """
        self._request = request

    @property
    def status(self):
        """
        :return core.register_board.request.RequestStatus:
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param core.register_board.request.RequestStatus status:
        """
        self._status = status

    @property
    def type(self):
        """
        :return core.register_board.constants.InfoType:
        """
        return self._type

    @property
    def value(self):
        """
        :return *:
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        :param * value:
        """
        self._value = value

    @property
    def unit_tags(self):
        """
        :return int:
        """
        return self._unit_tags

    @property
    def location(self):
        return self._location

    def __eq__(self, other):
        """ Equals """
        return (
                isinstance(Info, other)
                and self.type == other.type
                and self.status == other.status
                and self.unit_tags == other.unit_tags
                and self.location == other.location
                )
