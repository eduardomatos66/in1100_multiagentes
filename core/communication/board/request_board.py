#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.communication.board.generic_board import GenericBoard
from core.communication.constants.request_priority import RequestPriority


class RequestBoard(GenericBoard):
    """ Board for task request """

    def search_request_by_operation_ids(self, operation_ids):
        """
        :param core.register_board.constants.OperationTypeId operation_id:
        :return list[core.communication.item.request.Request]:
        """
        list_higher = []
        list_high = []
        list_medium = []
        list_low = []
        list_lower = []

        for request in self.board:
            if request.operation_type_id in operation_ids:
                if request.request_priority_level == RequestPriority.PRIORITY_HIGHER:
                    list_higher.append(request)
                elif request.request_priority_level == RequestPriority.PRIORITY_HIGH:
                    list_high.append(request)
                elif request.request_priority_level == RequestPriority.PRIORITY_MEDIUM:
                    list_medium.append(request)
                elif request.request_priority_level == RequestPriority.PRIORITY_LOW:
                    list_low.append(request)
                elif request.request_priority_level == RequestPriority.PRIORITY_LOWER:
                    list_lower.append(request)

        return list_higher + list_high + list_medium + list_low + list_lower

    def get_requests_by_status(self, status):
        """
        Get all requests by status
        :param core.communication.constants.request_status.RequestStatus status:
        :return list[core.communication.item.request.Request]:
        """
        return filter(lambda request: request.status == status, self.board)