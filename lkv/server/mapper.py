from lkv.server.handlers import *

command_table = {
    'get': handle_get_key, 
    'set': handle_set_key, 
    'del': handle_del_key, 
    'count': handle_count_keys,
    'ping': handle_ping_client,
    'keys': handle_match_keys,
    'clear': handle_clear_keys
}