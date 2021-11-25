from lkv.server.socket import web 

def run():
    host = 'localhost' 
    port = 9876
    import eventlet
    eventlet.wsgi.server(eventlet.listen((host, port)), web)

if __name__ == '__main__':
    run()