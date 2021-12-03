from lkv.cli.mapper import cmd_table
from lkv.config import HOST, PORT
from lkv.cli.errors import (
    CliError,
    WrongArityError,
    NoCommandError,
    ConnError
)
import socketio.exceptions
import socketio
import argparse
import time
import sys

def configure_argparser(parser: argparse.ArgumentParser):
    parser.add_argument('command', nargs='+', help='lkv commands')
    parser.add_argument('-h', '--host', dest='host', type=str, default=None, help='host client should connect to')
    parser.add_argument('-p', '--port', dest='port', type=int, default=None, help='port client should connect to')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')

def main(): 
    argp = argparse.ArgumentParser(description='LittleKV CLI', add_help=False)
    configure_argparser(argp)
    args = argp.parse_args() 
    
    host = args.host or HOST
    port = args.port or PORT
    command = args.command
    client = socketio.Client()

    try:
        try:

            client.connect(f'ws://{host}:{port}', transports='websocket') 
        except socketio.exceptions.ConnectionError:
            raise ConnError(host, port)

        op = command[0]
        params = command[1:]
        cmd_pair = cmd_table.get(op, None) 

        if not cmd_pair:
            raise NoCommandError(op) 

        arity, fn = cmd_pair
        
        if len(params) != arity:
            raise WrongArityError(op)

        fn(params, client, op)
    except CliError as e:
        print(str(e))
        
    finally:
        time.sleep(0.5)
        client.disconnect()

if __name__ == '__main__':
    main()

