# coding=utf-8

from sc2.position import Point2
from sc2.position import Point3


def distance(unit_a, unit_b):
    """
    Calculates the distance between two coordinates
    :param unit_a:
    :param unit_b:
    :return:
    """
    return unit_a.position.to2.distance_to(unit_b.position.to2)


def contains_unit(unit, unit_group):
    """
    Verify if determined unit is not contained a group of units
    :param unit:
    :param unit_group:
    :return:
    """
    for u in unit_group:
        if unit.tag == u.tag:
            return True
    return False


def get_units_tags(units):
    """ Helper method that returns a list of unit tags"""
    result = list()
    for u in units:
        result.append(u.tag)
    return result


def get_mean_location(pos1, pos2):
    """
    Get mean location between 2 points
    :param sc2.position.Point3 pos1:
    :param sc2.position.Point3 pos2:
    :return mean location:
    """
    x = (pos1.x + pos2.x) / 2
    y = (pos1.y + pos2.y) / 2

    if isinstance(pos1, Point2):
        pos1_z = 0
    else:
        pos1_z = pos1.z

    if isinstance(pos2, Point2):
        pos2_z = 0
    else:
        pos2_z = pos2.z

    z = (pos1_z + pos2_z) / 2

    return Point3((x, y, z))


def add_to_location(pos, value):
    """
    Increment location.
    :param sc2.position.Point2 pos:
    :param int value:
    :return sc2.position.Point2:
    """
    x = pos.x + value
    y = pos.y + value
    return Point2((x,y))
