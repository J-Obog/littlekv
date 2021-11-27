import socketio
from lkv.socket.server import server, global_store
from lkv.utils import parse_config

def run():
    cfg = parse_config()
    
    host = cfg['Connection']['host'] 
    port = cfg['Connection']['port']
    kvs_file_path = f"{cfg['FileSys']['filedir']}/{cfg['FileSys']['filename']}"

    global_store.init_store(kvs_file_path)
    web = socketio.WSGIApp(server)

    import eventlet
    eventlet.wsgi.server(eventlet.listen((host, int(port))), web)

if __name__ == '__main__':
    run()