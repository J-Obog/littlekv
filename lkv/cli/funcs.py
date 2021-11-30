from socketio import Client
from typing import List

def get_key(params: List[str], c: Client, cmd_name: str):
    print('It works!')
    #k = params[0]
    #c.emit(cmd_name, {'key': k})

def set_key(params: List[str], c: Client, cmd_name: str):
    k = params[0]
    v = params[1]
    c.emit(cmd_name, {'key': k, 'val': v})

def delete_key(params: List[str], c: Client, cmd_name: str):
    k = params[0]
    c.emit(cmd_name, {'key': k})

def count_keys(params: List[str], c: Client, cmd_name: str):
    c.emit(cmd_name, {})