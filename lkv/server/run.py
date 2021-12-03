from lkv.server.ws import socket_server
from lkv.config import HOST, PORT
import geventwebsocket as geventws
import socketio
import argparse

def configure_argparser(parser: argparse.ArgumentParser):
    parser.add_argument('-h', '--host', dest='host', type=str, default=None, help='host server should run on')
    parser.add_argument('-p', '--port', dest='port', type=int, default=None, help='port server should run on')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')
    
def main():
    argp = argparse.ArgumentParser(description="LittleKV Server", add_help=False)
    configure_argparser(argp)
    args = argp.parse_args() 

    host = args.host or HOST
    port = args.port or PORT

    web_server = geventws.WebSocketServer((host, port), socketio.WSGIApp(socket_server))
    print(f'Server listening @ {host} on port {port}')
    
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        print('Server shutting down') 
        web_server.close()
        exit(0)


if __name__ == '__main__':
    main()