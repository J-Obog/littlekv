from lkv.socket.server import web_server
from lkv.config import HOST, PORT

def run():
    import eventlet
    eventlet.wsgi.server(eventlet.listen((HOST, PORT)), web_server)

if __name__ == '__main__':
    run()