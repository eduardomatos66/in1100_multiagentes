# coding=utf-8

from core.logger import LOGGER


class GenericBoard(object):
    """ Generic Board """

    def __init__(self):
        self._board = []
        self._id_count = 0

    @property
    def board(self):
        """
        :return list[]:
        """
        return self._board

    def register(self, communication_item):
        """
        :param core.communication.item.communication_item.CommunicationItem communication_item:
        """
        LOGGER('Registering request: {}'.format(communication_item))

        if communication_item not in self._board:
            communication_item.id = self._id_count
            self._board.append(communication_item)
            self._id_count += 1
        else:
            LOGGER('Item {} is already on board.'.format(communication_item))

    def remove(self, communication_item):
        """
        :param core.communication.item.communication_item.CommunicationItem communication_item:
        """
        LOGGER('Removing communication item: {}'.format(communication_item))
        if communication_item in self._board:
            self._board.remove(communication_item)
