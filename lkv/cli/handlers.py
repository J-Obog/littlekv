from socketio import Client
from typing import List

def handle_command_response(res: any):
    print(res)

def handle_get_key(params: List[str], c: Client, cmd_name: str):
    k = params[0]
    c.emit(cmd_name, {'key': k}, callback=handle_command_response)

def handle_set_key(params: List[str], c: Client, cmd_name: str):
    k = params[0]
    v = params[1]
    c.emit(cmd_name, {'key': k, 'val': v}, callback=handle_command_response)

def handle_delete_key(params: List[str], c: Client, cmd_name: str):
    k = params[0]
    c.emit(cmd_name, {'key': k}, callback=handle_command_response)

def handle_count_keys(params: List[str], c: Client, cmd_name: str):
    c.emit(cmd_name, {}, callback=handle_command_response)

def handle_match_keys(params: List[str], c: Client, cmd_name: str):
    pattern = params[0]
    c.emit(cmd_name, {'pattern': pattern}, callback=handle_command_response)

def handle_ping_server(params: List[str], c: Client, cmd_name: str):
    c.emit(cmd_name, {}, callback=handle_command_response)
