import os
from lkv.utils import parse_config

cfg = parse_config() 

HOST = cfg['Connection']['host']
PORT = int(cfg['Connection']['port'])
STORE_PATH = os.path.join(os.getcwd(), cfg['FileSys']['dirname'])