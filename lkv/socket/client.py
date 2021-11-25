import socketio

client = socketio.Client() 

@client.on('cmd_reply')
def handle_response(data):
    pass