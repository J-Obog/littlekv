from lkv.cli.map import cmd_table
from lkv.client import client
from lkv.config import HOST, PORT
from socketio.exceptions import ConnectionError
from lkv.cli.errors import (
    CliError,
    WrongArityError,
    NoCommandError,
    ConnError
)

import time
import sys

def main() -> None:
    try:
        try:
            client.connect(f'ws://{HOST}:{PORT}', transports='websocket') 
        except ConnectionError:
            raise ConnError(HOST, PORT)

        args = sys.argv

        if len(args) == 1:
            quit()

        op = args[1]
        params = args[2:]
        cmd_pair = cmd_table.get(op, None) 

        if not cmd_pair:
            raise NoCommandError(op) 

        arity, fn = cmd_pair
        
        if len(params) != arity:
            raise WrongArityError(op)

        fn(params, client, op)
    except CliError as e:
        print(str(e))
        exit(e.code)
    finally:
        time.sleep(0.5)
        client.disconnect()


if __name__ == '__main__':
    main()

