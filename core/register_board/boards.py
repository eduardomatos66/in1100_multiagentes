#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BoardRequest(object):
    """ Board for task request """

    def __init__(self):
        self._board = []
        self._requests_count = 0

    def register(self, request):
        """
        :param core.request_board.request.Request request:
        """
        request.request_id = self._requests_count
        self._board.append(request)
        self._requests_count += 1

    @property
    def board(self):
        """
        :return list[core.register_board.request.Request]:
        """
        return self._board


class BoardInfo(object):
    """ Board for share information between bots """

    def __init__(self):
        self._board = []
        self._info_count = 0

    def register(self, info):
        """
        :param core.register_board.info.Info info:
        """
        info.info_id = self._info_count
        self._board.append(info)
        self._info_count += 1

    @property
    def board(self):
        """
        :return list[core.register_board.info.Info:
        """
        return self._board