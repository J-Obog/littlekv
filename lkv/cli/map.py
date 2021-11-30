from lkv.cli.funcs import *

cmd_table = {
    'get': (1, get_key), 
    'set': (2, set_key), 
    'del': (1, delete_key), 
    'count': (0, count_keys),
    'ping': (0, ping_server),
}