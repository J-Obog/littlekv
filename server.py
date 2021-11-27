from lkv.socket.server import store, web_server
from lkv.socket.config import *

def run():
    store.init_store(KV_FILE_PATH)

    import eventlet
    eventlet.wsgi.server(eventlet.listen((HOST, int(PORT))), web_server)

if __name__ == '__main__':
    run()