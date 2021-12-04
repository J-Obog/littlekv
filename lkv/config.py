import os
from lkv.utils import parse_config

cfg = parse_config() 
HOST = cfg['Connection']['host']
PORT = int(cfg['Connection']['port'])
KV_DIR = os.path.join(os.getcwd(), cfg['FileSys']['kv_dir'])
KV_SOURCE = os.path.join(KV_DIR, cfg['FileSys']['kv_source'])