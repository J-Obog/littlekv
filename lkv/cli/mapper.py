from lkv.cli.handlers import *

cmd_table = {
    'get': (1, handle_get_key), 
    'set': (2, handle_set_key), 
    'del': (1, handle_delete_key), 
    'count': (0, handle_count_keys),
    'ping': (0, handle_ping_server),
    'keys': (1, handle_match_keys),
    'clear': (0, handle_clear_keys)
}