from socketio.exceptions import ConnectionError
from lkv.flags import parse_cli_args
import socketio
import time

def response_to_stdout(*args):
    res = args[0]
    err = args[1] 
    msg = res if not err else err
    print(msg)

def main(): 
    args = parse_cli_args()
    
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

