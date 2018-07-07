#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.communication.board.generic_board import GenericBoard


class InfoBoard(GenericBoard):
    """ Board for task request """

    def search_request_by_type(self, info_type):
        """

        :param info_type:
        :return:
        """
        return [info for info in self.board if info.type == info_type]
