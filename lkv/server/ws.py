import socketio
from lkv.server.mapper import command_table
from lkv.server.exceptions import (
    LKVError,
    NoCommandProvidedError,
    NoParamsProvidedError,
    NoCommandError
)

socket_server = socketio.Server(async_mode='gevent')

def handle_client_connected(sid, environ):
    print(f'Client {sid} connected')

def handle_client_disconected(sid):
    print(f'Client {sid} disconnected')

def handle_lkv_command(sid, data):
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
        
        return (cmd_handler(cmd, params, len(params)), None)
    except LKVError as e:
        return (None, str(e))

socket_server.on('connect', handle_client_connected)
socket_server.on('disconnect', handle_client_disconected)
socket_server.on('lkv:command', handle_lkv_command)