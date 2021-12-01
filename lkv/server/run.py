from lkv.server import web_server
from lkv.config import HOST, PORT
from geventwebsocket.server import WebSocketServer
import signal

def main():    
    s = WebSocketServer((HOST, PORT), web_server)

    def shutdown():
        s.close()

    signal.signal(signal.SIGTERM, shutdown)
    s.serve_forever()


if __name__ == '__main__':
    main()