import socketio
from lkv.store import KVStore

server = socketio.Server(always_connect=True, allow_upgrades=False)
global_store = KVStore()

@server.event
def connect(sid, environ):
    print('Welcome', sid)

@server.event
def disconnect(sid):
    print('Goodbye', sid)

@server.on('get')
def get_key(sid, data):
    res = global_store.getk(data['key'])
    server.emit('cmd_reply', {'res': res})

@server.on('set')
def set_key(sid, data):
    res = global_store.setk(data['key'], data['val'])
    server.emit('cmd_reply', {'res': res})

@server.on('del')
def del_key(sid, data):
    res = global_store.delk(data['key'])
    server.emit('cmd_reply', {'res': res})

@server.on('count')
def count_keys(sid, data):
    res = global_store.countk()
    server.emit('cmd_reply', {'res': res})