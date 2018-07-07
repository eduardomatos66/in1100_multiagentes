# coding=utf-8


class CommunicationItem(object):
    """ CommunicationItem Item """

    def __init__(self, item_id, iteration):
        """
        Init method
        :param int item_id:
        :param int iteration:
        """
        self._item_id = item_id
        self._iteration = iteration

    @property
    def item_id(self):
        """
        Get item id
        :return int:
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Set item id
        :param int item_id:
        """
        self._item_id = item_id

    @property
    def iteration(self):
        """
        :return in:
        """
        return self._iteration
