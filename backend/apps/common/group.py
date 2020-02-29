
class Group(object):
    def __init__(self, group_id):
        self.group_id = str(group_id)
        self.sockets = set()
        self.headers = list()
        self.body = [[]]

    @property
    def socket_data(self):
        return {
            'headers': self.headers,
            'body': self.body
        }

    async def _update_sockets(self):
        for ws in [_ for _ in self.sockets if _ is not None]:
            await ws.send_json(self.socket_data)

    def _get_name_index(self, name):
        return self.headers.index(name)

    async def join(self, name, ws=None):
        self.sockets.add(ws)
        self.headers.append(name)
        self.body = [_+[''] for _ in self.body]
        await self._update_sockets()
        print(f'{name} joined to {self.group_id}')

    async def leave(self, name, ws=None):
        if ws is not None:
            self.sockets.remove(ws)
        i = self._get_name_index(name)
        self.headers.pop(i)
        for row in self.body:
            row.pop(i)
        await self._update_sockets()
        print(f'{name} leaved {self.group_id}')

    async def add_value(self, name, value):
        i = self._get_name_index(name)
        for rows in self.body:
            if rows[i] == '':
                rows[i] = str(value)
                break
        else:
            new_row = [''] * len(self.headers)
            new_row[i] = str(value)
            self.body.append(new_row)
        await self._update_sockets()
        print(f'{name} updated {self.group_id}')

    async def clear(self, name):
        self.body = [[''] * len(self.headers)]
        await self._update_sockets()
        print(f'{name} cleared {self.group_id}')
