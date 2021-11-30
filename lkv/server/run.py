from lkv.server import web_server
from lkv.config import HOST, PORT
import time

def main():
    from geventwebsocket.server import WebSocketServer
    svr = WebSocketServer((HOST, PORT), web_server)
    svr.serve_forever()

if __name__ == '__main__':
    main()