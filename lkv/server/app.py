import socketio
from lkv.server.socket import create_server_conn
from lkv.utils import parse_config

def run(host, port):
    server = create_server_conn()
    web = socketio.WSGIApp(server)
    
    import eventlet
    eventlet.wsgi.server(eventlet.listen((host, port)), web)

if __name__ == '__main__':
    cfg = parse_config()
    host = cfg['Connection']['host']
    port = cfg['Connection']['port']
    
    run(host, int(port))