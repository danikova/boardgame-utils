from aiohttp import web
import json as JSON
import aiohttp


async def check_username(request):
    group_id, name = request.query.get('groupId'), request.query.get('name')
    manager = request.app['group_manager']
    group = manager.get_group_by_id(group_id)
    if group is not None and name in group.headers:
        return web.Response(status=403)
    return web.Response(status=200)


async def scoreboard_websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    group_id, name = request.query.get('groupId'), request.query.get('name')
    if name is None or group_id is None:
        await ws.send_json({
            'error': 'not valid name or group id'
        })
        await ws.close()

    manager = request.app['group_manager']
    group = manager.get_or_create_group_by_id(group_id)
    if name in group.headers:
        await ws.send_json({
            'error': 'this name has already taken'
        })
        await ws.close()

    await group.join(name, ws)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                try:
                    json = msg.json()
                    _type, _data = json.get('type'), json.get('data')
                    if _type == 'add_value' and _data is not None:
                        await group.add_value(name, _data)
                    if _type == 'clear':
                        await group.clear(name)

                except JSON.JSONDecodeError:
                    pass
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    await group.leave(name, ws)
    manager.remove_group_when_it_has_no_connections(group_id)

    return ws
