#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from core.communication.constants.request_status import RequestStatus
from core.communication.item.communication_item import CommunicationItem


class Request(CommunicationItem):
    """ An action request """

    def __init__(self, item_id, iteration, operation_type_id=None, request_priority=None, location=None,
                 unit_type_id=None, unit_tags=None, amount=0):
        """
        Initializer.
        :param int item_id:
        :param int iteration:
        :param core.register_board.constants.OperationTypeId operation_type_id:
        :param core.register_board.constants.RequestPriority request_priority:
        :param sc2.position.Point2 location:
        :param sc2.ids.unit_typeid.UnitTypeId unit_type_id:
        :param list[str] unit_tags:
        :param int amount:
        """
        super(Request, self).__init__(item_id=item_id, iteration=iteration)

        self._operation_type_id = operation_type_id
        self._request_priority_level = request_priority
        self._location = location
        self._unit_type_id = unit_type_id
        self._unit_tags = unit_tags
        self._status = RequestStatus.TO_BE_DONE
        self._amount = amount

    def __str__(self):
        return json.dumps(
            dict(
                request_id=self._item_id,
                operation_type_id=self._operation_type_id.name if self._operation_type_id else '',
                unit_type_id=self._unit_type_id.name if self._unit_type_id else '',
                request_priority_level=self._request_priority_level.name,
                amount=self._amount,
                status=self._status.name
            )
        )

    def __eq__(self, other):
        """
        Equals.
        :param core. other:
        :return:
        """
        result = isinstance(other, Request)
        if result:
            result = self.unit_type_id == other.unit_type_id \
                     and self.status == other.status and self.status == RequestStatus.TO_BE_DONE \
                     and self.request_priority_level == other.request_priority_level
        else:
            return False

        return result or self._item_id == other.item_id

    @property
    def operation_type_id(self):
        """
        :return sc2.ids.unit_typeid.UnitTypeId:
        """
        return self._operation_type_id

    @property
    def request_priority_level(self):
        """
        :return core.register_board.constants.RequestPriority:
        """
        return self._request_priority_level

    @request_priority_level.setter
    def request_priority_level(self, request_priority_level):
        """
        :param core.register_board.constants.RequestPriority request_priority_level:
        """
        self._request_priority_level = request_priority_level

    @property
    def location(self):
        """
        :return sc2.position.Point2:
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        :param sc2.position.Point2 location:
        """
        self._location = location

    @property
    def unit_type_id(self):
        """
        :return sc2.ids.unit_typeid.UnitTypeId:
        """
        return self._unit_type_id

    @unit_type_id.setter
    def unit_type_id(self, unit_type_id):
        """
        :param sc2.ids.unit_typeid.UnitTypeId unit_type_id:
        """
        self._unit_type_id = unit_type_id

    @property
    def unit_tags(self):
        """
        :return list[str]:
        """
        return self._unit_tags

    @unit_tags.setter
    def unit_tags(self, unit_tags):
        """
        :param list[str] unit_tags:
        """
        self._unit_tags = unit_tags

    @property
    def status(self):
        """
        :return core.register_board.constants.RequestStatus:
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        :param core.register_board.constants.RequestStatus status:
        """
        self._status = status

    @property
    def amount(self):
        """
        :return int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        :param int amount:
        """
        self._amount = amount
