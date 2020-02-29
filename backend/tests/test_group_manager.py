import unittest
from apps.common.group_manager import GroupManager


class TestGroupManager(unittest.TestCase):
    def test_group_manager_get_or_create_group_by_id(self):
        gm = GroupManager()
        g1 = gm.get_or_create_group_by_id(123123)
        assert len(gm.groups.keys()) == 1
        gm.get_or_create_group_by_id(123123)
        assert len(gm.groups.keys()) == 1
        gm.get_or_create_group_by_id(321321)
        assert len(gm.groups.keys()) == 2

    def test_group_manager_remove_group_when_it_has_no_connections(self):
        gm = GroupManager()
        g1 = gm.get_or_create_group_by_id(123123)
        g1.sockets = {'asd', 'asd1'}
        gm.remove_group_when_it_has_no_connections(123123)
        assert len(gm.groups.keys()) == 1
        g1.sockets = set()
        gm.remove_group_when_it_has_no_connections(123123)
        assert len(gm.groups.keys()) == 0
