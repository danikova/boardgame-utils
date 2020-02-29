import unittest
from apps.common.group import Group


async def test_group_join():
    g = Group(123123)
    g.body = [
        ['asd'], ['asd']
    ]
    await g.join('test user')
    for row in g.body:
        assert ['asd', ''] == row
    assert ['test user'] == g.headers


async def test_group_mass_join_and_leave():
    g = Group(123123)
    await g.join('test1')
    await g.join('test2')
    await g.join('test3')
    await g.join('test4')
    assert g.headers == ['test1', 'test2', 'test3', 'test4']
    assert len(g.body[0]) == 4
    await g.leave('test2')
    await g.leave('test3')
    assert g.headers == ['test1', 'test4']
    assert len(g.body[0]) == 2


async def test_group_add_value():
    g = Group(123123)
    await g.join('test1')
    await g.add_value('test1', 5)
    await g.add_value('test1', 5)
    await g.add_value('test1', 5)
    await g.add_value('test1', 5)
    assert len(g.body[0]) == 1
    assert g.body[0][0] == '5'
    assert g.body[3][0] == '5'
    await g.join('test2')
    await g.add_value('test2', 10)
    await g.add_value('test2', 10)
    await g.add_value('test1', 5)
    assert len(g.body[0]) == 2
    assert g.body[0][0] == '5'
    assert g.body[4][0] == '5'
    assert g.body[0][1] == '10'
    assert g.body[1][1] == '10'


async def test_group_clear():
    g = Group(123123)
    await g.join('test1')
    await g.join('test2')
    await g.add_value('test1', 5)
    await g.add_value('test2', 5)
    await g.add_value('test1', 5)
    await g.add_value('test2', 5)
    assert len(g.body[0]) == 2
    assert len(g.body) == 2
    await g.clear('test1')
    assert g.body == [['', '']]
