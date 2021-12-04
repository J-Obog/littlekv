from lkv.config import HOST, PORT
from socketio.exceptions import ConnectionError
import socketio
import argparse
import time

def configure_argparser(parser: argparse.ArgumentParser):
    parser.add_argument('command', nargs='+', help='lkv commands')
    parser.add_argument('-h', '--host', dest='host', type=str, default=HOST, help='host client should connect to')
    parser.add_argument('-p', '--port', dest='port', type=int, default=PORT, help='port client should connect to')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')

def response_to_stdout(*args):
    res = args[0]
    err = args[1] 
    msg = res if not err else err
    print(msg)

def main(): 
    argp = argparse.ArgumentParser(description='LittleKV CLI', add_help=False)
    configure_argparser(argp)
    args = argp.parse_args() 
    
    host = args.host
    port = args.port
    command = args.command
    op = command[0]
    params = command[1:]

    try:
        client = socketio.Client()
        client.connect(f'ws://{host}:{port}')
        client.emit('lkv:command', {'cmd': op, 'params': params}, callback=response_to_stdout)
        time.sleep(0.5)
        client.disconnect()
    except ConnectionError:
        print(f'Unable to connect to host {host} on port {port}')
        exit(0)

if __name__ == '__main__':
    main()

