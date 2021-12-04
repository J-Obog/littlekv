from typing import List, Dict
from lkv.store import KVStore

def handle_ping_client(params: List[str], store: KVStore) -> str:
    return 'PONG'

def handle_get_key(params: List[str], store: KVStore) -> str:
    k = params[0]
    v = store.getk(k)
    return v if v != None else '<None>'

def handle_set_key(params: List[str], store: KVStore) -> str:
    k = params[0]
    v = params[1]
    store.setk(k,v)
    return 'OK'

def handle_del_key(params: List[str], store: KVStore) -> str:
    k = params[0]
    store.delk(k)
    return 'OK'

def handle_count_keys(params: List[str], store: KVStore) -> int:
    return store.countk()
 
def handle_match_keys(params: List[str], store: KVStore) -> Dict[str, str]:
    return store.getk()

def handle_clear_keys(params: List[str], store: KVStore) -> str:
    store.cleark()
    return 'OK'