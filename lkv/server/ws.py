import socketio
import geventwebsocket as geventws
from lkv.server.mapper import command_table
from lkv.store import KVStore
from lkv.server.exceptions import (
    LKVError,
    NoCommandError,
    NoCommandProvidedError,
    NoParamsProvidedError
)

class LKVSockServer(socketio.Server):
    def __init__(self, data_store: KVStore):
        super().__init__(async_mode='gevent')
        self.__kv_store = data_store
        self.on('connect', self.client_connected)
        self.on('disconnect', self.client_disconnected)
        self.on('lkv:command', self.handle_lkv_command)

    def listen(self, host: str, port: int):
        server = geventws.WebSocketServer((host, port), socketio.WSGIApp(self))
        print(f'Server listening @ {host} on port {port}')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Server shutting down') 
            server.close()
            exit(0)

    def client_connected(self, sid, environ):
        print(f'Client {sid} connected')

    def client_disconnected(self, sid):
        print(f'Client {sid} disconnected')

    def handle_lkv_command(self, sid, data):
        try:
            if 'cmd' not in data: 
                raise NoCommandProvidedError
            
            if 'params' not in data: 
                raise NoParamsProvidedError

            cmd = data['cmd']
            params = data['params']
            cmd_handler = command_table.get(cmd, None)
            
            if not cmd_handler: 
                raise NoCommandError(cmd) 

            return (cmd_handler(cmd, params, len(params), self.__kv_store), None)
        except LKVError as e:
            return (None, str(e))