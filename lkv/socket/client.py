import socketio
from lkv.socket.config import *

client = socketio.Client()

@client.on('cmd_reply')
def handle_response(data):
    print(data['res'])

client.connect(f'ws://{HOST}:{PORT}', transports='websocket')