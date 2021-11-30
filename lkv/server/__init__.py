import socketio
from lkv.store import KVStore

server = socketio.Server(always_connect=True, allow_upgrades=False)
web_server = socketio.WSGIApp(server)
store = KVStore()

@server.event
def connect(sid, environ):
    print(f'Client {sid} connected')

@server.event
def disconnect(sid):
    print(f'Client {sid} disconnected')

@server.on('get')
def get_key(sid, data):
    try:
        res = store.getk(data['key'])
        server.emit('cmd_reply', {'res': res})
    except Exception as e:
        server.emit('cmd_reply', {'res': str(e)})

@server.on('set')
def set_key(sid, data):
    try:
        store.setk(data['key'], data['val'])
        server.emit('cmd_reply', {'res': 'OK'})
    except Exception as e:
        server.emit('cmd_reply', {'res': str(e)})

@server.on('del')
def del_key(sid, data):
    try:
        store.delk(data['key'])
        server.emit('cmd_reply', {'res': 'OK'})
    except Exception as e:
        server.emit('cmd_reply', {'res': str(e)})

@server.on('count')
def count_keys(sid, data):
    try:
        res = store.countk()
        server.emit('cmd_reply', {'res': res})
    except Exception as e:
        server.emit('cmd_reply', {'res': str(e)})