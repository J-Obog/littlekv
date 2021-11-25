import socketio

server = socketio.Server()

@server.event
def connect(sid, environ):
    print('Welcome', sid)

@server.event
def disconnect(sid):
    print('Goodbye', sid)