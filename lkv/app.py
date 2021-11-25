import socketio
from lkv.socket.server import server

def run():
    host = 'localhost' 
    port = 9876
    web = socketio.WSGIApp(server)
    
    import eventlet
    eventlet.wsgi.server(eventlet.listen((host, port)), web)

if __name__ == '__main__':
    run()