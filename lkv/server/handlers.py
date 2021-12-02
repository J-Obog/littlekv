from typing import Dict
from lkv.server import kv_store

def handle_client_connected(sid, environ):
    print(f'Client {sid} connected')

def handle_client_disconected(sid):
    print(f'Client {sid} disconnected')

def handle_ping_client(sid: str, data: any) -> str:
    return 'PONG'

def handle_get_key(sid: str, data: any) -> str:
    v = kv_store.getk(data['key'])
    return v if v != None else '<None>'

def handle_set_key(sid: str, data: any) -> str:
    kv_store.setk(data['key'], data['val'])
    return 'OK'

def handle_del_key(sid: str, data: any) -> str:
    kv_store.delk(data['key'])
    return 'OK'

def handle_count_keys(sid: str, data: any) -> int:
    return kv_store.countk()
 
def handle_match_keys(sid: str, data: any) -> Dict[str, str]:
    return kv_store.getk()

def handle_clear_keys(sid: str, data: any) -> str:
    kv_store.cleark()
    return 'OK'