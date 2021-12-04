from lkv.server.ws import LKVSockServer
from lkv.store import KVStore
from lkv.config import HOST, PORT, STORE_PATH
import argparse

def configure_argparser(parser: argparse.ArgumentParser):
    parser.add_argument('-h', '--host', dest='host', type=str, default=HOST, help='host server should run on')
    parser.add_argument('-p', '--port', dest='port', type=int, default=PORT, help='port server should run on')
    parser.add_argument('-d', '--dir', dest='kv_dir', type=str, default=STORE_PATH, help='directory of target kv file')
    parser.add_argument('-s', '--src', dest='kv_src', type=str, default='dump.kv', help='name of target kv file')
    parser.add_argument('-H', '--help', action='help', help='show this help message and exit')
    
def main():
    argp = argparse.ArgumentParser(description='LittleKV Server', add_help=False)
    configure_argparser(argp)
    args = argp.parse_args()

    host = args.host
    port = args.port
    kv_dir = args.kv_dir
    kv_source = args.kv_src

    socket_server = LKVSockServer(KVStore(kv_dir, kv_source))
    socket_server.listen(host, port)


if __name__ == '__main__':
    main()