import socketio

def create_server_conn():
    server = socketio.Server()
    
    @server.event
    def connect(sid, environ):
        print(sid, 'connected')

    @server.event
    def disconnect(sid, environ):
        print(sid, 'disconnected')

    return server