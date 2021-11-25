import socketio
from lkv.store import KVStore

server = socketio.Server()
global_store = KVStore()

@server.event
def connect(sid, environ):
    print('Welcome', sid)

@server.event
def disconnect(sid):
    print('Goodbye', sid)