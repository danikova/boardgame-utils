from aiohttp import web
from apps.Scoreboard import scoreboard_websocket_handler, check_username
from apps.common.group_manager import GroupManager

app = web.Application()
app.router.add_get('/scoreboard/', scoreboard_websocket_handler)
app.router.add_get('/scoreboard/check-name/', check_username)


async def on_startup(app):
    app['group_manager'] = GroupManager()


app.on_startup.append(on_startup)

if __name__ == '__main__':
    web.run_app(app)
