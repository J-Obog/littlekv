from typing import List, Dict
from lkv.server.exceptions import BadArityError
from lkv.store import KVStore

def handle_ping_client(cmd: str, params: List[str], param_len: int, store: KVStore) -> str:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)
    
    return 'PONG'

def handle_get_key(cmd: str, params: List[str], param_len: int, store: KVStore) -> str:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)
    
    k = params[0]
    v = store.getk(k)
    return v if v != None else '<None>'

def handle_set_key(cmd: str, params: List[str], param_len: int, store: KVStore) -> str:
    if param_len != 2:
        raise BadArityError(cmd, param_len, 2)

    k = params[0]
    v = params[1]
    store.setk(k,v)
    return 'OK'

def handle_del_key(cmd: str, params: List[str], param_len: int, store: KVStore) -> str:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)

    k = params[0]
    store.delk(k)
    return 'OK'

def handle_count_keys(cmd: str, params: List[str], param_len: int, store: KVStore) -> int:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)

    return store.countk()
 
def handle_match_keys(cmd: str, params: List[str], param_len: int, store: KVStore) -> Dict[str, str]:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)

    return store.getk()

def handle_clear_keys(cmd: str, params: List[str], param_len: int, store: KVStore) -> str:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)

    store.cleark()
    return 'OK'