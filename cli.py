from lkv.socket.client import client
import time
import typer

DELAY = 0.25
app = typer.Typer()

@app.command('set')
def set(key: str, val: str):
    client.emit('set', {'key': key, 'val': val})
    time.sleep(DELAY)
    client.disconnect()

@app.command('get')
def get(key: str):
    client.emit('get', {'key': key})
    time.sleep(DELAY)
    client.disconnect()

@app.command('del')
def delete(key: str):
    client.emit('del', {'key': key})
    time.sleep(DELAY)
    client.disconnect()

@app.command('count')
def count():
    client.emit('count', {})
    time.sleep(DELAY)
    client.disconnect()

if __name__ == "__main__":
    app()