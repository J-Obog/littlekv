from lkv.socket.client import client
from lkv.utils import parse_config

def get_conn_url():
    cfg = parse_config()
    host = cfg['Connection']['host'] 
    port = cfg['Connection']['port']
    return f'ws://{host}:{port}'

""" Command Line Interface """
def main():
    client.connect(get_conn_url())

    while True:
        cmd = input('lkv-cli> ') 
        params = cmd.split(' ') 
        op = params[0].lower()

        if op == 'exit' and len(params) == 1:
            client.disconnect()
            quit()
        else:
            if op == 'get':
                client.emit('get', {'key': params[1]})
            elif op == 'set':
                client.emit('set', {'key': params[1], 'val': params[2]})
            elif op == 'del':
                client.emit('del', {'key': params[1]})
            elif op == 'count':
                client.emit('count', {})
            else:
                print('INVALID COMMAND')

if __name__ == '__main__':
    main()