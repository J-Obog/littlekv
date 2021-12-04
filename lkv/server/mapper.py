from lkv.server.handlers import *

command_table = {
    'get': (handle_get_key, 1), 
    'set': (handle_set_key, 2), 
    'del': (handle_del_key, 1), 
    'count': (handle_count_keys, 0),
    'ping': (handle_ping_client, 0),
    'keys': (handle_match_keys, 1),
    'clear': (handle_clear_keys, 0)
}