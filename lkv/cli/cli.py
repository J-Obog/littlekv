from lkv.cli.map import cmd_table
from lkv.client import client
from lkv.config import HOST, PORT
import time
import sys

def main():
    client.connect(f'ws://{HOST}:{PORT}', transports='websocket') 
    args = sys.argv

    if len(args) == 1:
        quit()

    op = args[1]
    params = args[2:]
    cmd_pair = cmd_table.get(op, None) 

    if not cmd_pair:
        print(f'ERROR => Unknown command {op}')
        exit(873)

    arity, fn = cmd_pair
    
    if len(params) != arity:
        print(f'ERROR => Wrong number of arguments to {op} command')
        exit(683)

    fn(params, client, op)

    time.sleep(0.5)
    client.disconnect()

if __name__ == '__main__':
    main()

