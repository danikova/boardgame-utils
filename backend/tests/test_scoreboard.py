from aiohttp import web
from apps.common.group_manager import GroupManager
from apps.Scoreboard import check_username, scoreboard_websocket_handler


async def test_check_user_name_for_a_non_existing_group(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', check_username)
    manager = GroupManager()
    app['group_manager'] = manager

    client = await aiohttp_client(app)
    resp = await client.get('/?groupId=123123;name=testuser')
    assert resp.status == 200


async def test_check_user_name_for_an_empty_group(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', check_username)
    manager = GroupManager()
    manager.get_or_create_group_by_id(123123)
    app['group_manager'] = manager

    client = await aiohttp_client(app)
    resp = await client.get('/?groupId=123123;name=testuser')
    assert resp.status == 200


async def test_check_user_name_if_this_uname_is_in_the_headers(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', check_username)
    manager = GroupManager()
    group = manager.get_or_create_group_by_id(123123)
    await group.join('testuser')
    app['group_manager'] = manager

    client = await aiohttp_client(app)
    resp = await client.get('/?groupId=123123;name=testuser')
    assert resp.status == 403


async def test_scoreboard_websocket_connection_without_any_data(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', scoreboard_websocket_handler)
    manager = GroupManager()
    group = manager.get_or_create_group_by_id(123123)
    await group.join('testuser')
    app['group_manager'] = manager

    client = await aiohttp_client(app)
    ws = await client.ws_connect('/')
    json = await ws.receive_json()
    assert 'error' in json


async def test_scoreboard_websocket_connection_with_valid_data(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', scoreboard_websocket_handler)
    manager = GroupManager()
    group = manager.get_or_create_group_by_id(123123)
    app['group_manager'] = manager
    client = await aiohttp_client(app)
    ws = await client.ws_connect('/?groupId=123123;name=testuser')
    json = await ws.receive_json()
    assert 'body' in json
    assert 'headers' in json


async def test_scoreboard_websocket_connection_user_push_new_data(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', scoreboard_websocket_handler)
    manager = GroupManager()
    group = manager.get_or_create_group_by_id(123123)
    app['group_manager'] = manager
    client = await aiohttp_client(app)
    ws = await client.ws_connect('/?groupId=123123;name=testuser')
    old_json = await ws.receive_json()
    await ws.send_json({'type': 'add_value', 'data': '123'})
    new_json = await ws.receive_json()
    assert old_json['body'] == [['']]
    assert new_json['body'] == [['123']]


async def test_scoreboard_websocket_connection_user_push_clear_data(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', scoreboard_websocket_handler)
    manager = GroupManager()
    group = manager.get_or_create_group_by_id(123123)
    app['group_manager'] = manager
    client = await aiohttp_client(app)
    ws = await client.ws_connect('/?groupId=123123;name=testuser')
    await ws.receive_json()
    await ws.send_json({'type': 'add_value', 'data': '123'})
    old_json = await ws.receive_json()
    await ws.send_json({'type': 'clear'})
    new_json = await ws.receive_json()
    assert old_json['body'] == [['123']]
    assert new_json['body'] == [['']]
