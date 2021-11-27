import socketio
from lkv.utils import parse_config

client = socketio.Client()

@client.on('cmd_reply')
def handle_response(data):
    print(data['res'])

cfg = parse_config()
host = cfg['Connection']['host']
port = cfg['Connection']['port']

client.connect(f'ws://{host}:{port}', transports='websocket')