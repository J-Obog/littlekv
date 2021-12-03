from lkv.server.ws import socket_server
from lkv.config import HOST, PORT
import geventwebsocket as geventws
import socketio

def main():   
    web_server = geventws.WebSocketServer((HOST, PORT), socketio.WSGIApp(socket_server))
    print(f'Server listening @ {HOST} on port {PORT}')

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        print('Server shutting down') 
        web_server.close()
        exit(0)

if __name__ == '__main__':
    main()