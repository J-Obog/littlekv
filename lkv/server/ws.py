import socketio
from lkv.server.handlers import *

socket_server = socketio.Server(async_mode='gevent')

socket_server.on('connect', handle_client_connected)
socket_server.on('disconnect', handle_client_disconected)
socket_server.on('get', handle_get_key)
socket_server.on('set', handle_get_key)
socket_server.on('del', handle_del_key)
socket_server.on('count', handle_count_keys)
socket_server.on('keys', handle_match_keys)
socket_server.on('ping', handle_ping_client)