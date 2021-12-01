import socketio
from lkv.server.ws import socket_server
from lkv.config import HOST, PORT
import geventwebsocket as geventws

def main():
    web_server = geventws.WebSocketServer((HOST, PORT), socketio.WSGIApp(socket_server))
    print(f'Server listening @ {HOST} on port {PORT}')
    web_server.serve_forever()

if __name__ == '__main__':
    main()