from lkv.server.ws import LKVSockServer
from lkv.store import KVStore
from lkv.flags import parse_server_args

def main():
    args = parse_server_args()
    
    host = args.host
    port = args.port
    kv_dir = args.kv_dir
    kv_source = args.kv_src

    socket_server = LKVSockServer(KVStore(kv_dir, kv_source))
    socket_server.listen(host, port)


if __name__ == '__main__':
    main()