from lkv.config import HOST, PORT, STORE_PATH
import argparse

def parse_server_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='LittleKV Server', add_help=False)
    parser.add_argument('-h', '--host', dest='host', type=str, default=HOST, help='host server should run on')
    parser.add_argument('-p', '--port', dest='port', type=int, default=PORT, help='port server should run on')
    parser.add_argument('-d', '--dir', dest='kv_dir', type=str, default=STORE_PATH, help='directory of target kv file')
    parser.add_argument('-s', '--src', dest='kv_src', type=str, default='dump.kv', help='name of target kv file')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')
    return parser.parse_args()

def parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='LittleKV CLI', add_help=False)
    parser.add_argument('command', nargs='+', help='lkv commands')
    parser.add_argument('-h', '--host', dest='host', type=str, default=HOST, help='host client should connect to')
    parser.add_argument('-p', '--port', dest='port', type=int, default=PORT, help='port client should connect to')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')
    return parser.parse_args()