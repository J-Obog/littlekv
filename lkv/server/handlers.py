from typing import List, Dict
from lkv.server import kv_store
from lkv.server.exceptions import BadArityError

def handle_ping_client(cmd: str, params: List[str], param_len: int) -> str:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)
    
    return 'PONG'

def handle_get_key(cmd: str, params: List[str], param_len: int) -> str:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)
    
    k = params[0]
    v = kv_store.getk(k)
    return v if v != None else '<None>'

def handle_set_key(cmd: str, params: List[str], param_len: int) -> str:
    if param_len != 2:
        raise BadArityError(cmd, param_len, 2)

    k = params[0]
    v = params[1]
    kv_store.setk(k,v)
    return 'OK'

def handle_del_key(cmd: str, params: List[str], param_len: int) -> str:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)

    k = params[0]
    kv_store.delk(k)
    return 'OK'

def handle_count_keys(cmd: str, params: List[str], param_len: int) -> int:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)

    return kv_store.countk()
 
def handle_match_keys(cmd: str, params: List[str], param_len: int) -> Dict[str, str]:
    if param_len != 1:
        raise BadArityError(cmd, param_len, 1)

    return kv_store.getk()

def handle_clear_keys(cmd: str, params: List[str], param_len: int) -> str:
    if param_len != 0:
        raise BadArityError(cmd, param_len, 0)

    kv_store.cleark()
    return 'OK'