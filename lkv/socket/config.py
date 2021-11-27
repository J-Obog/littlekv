from lkv.utils import parse_config

cfg = parse_config()

HOST = cfg['Connection']['host']
PORT = cfg['Connection']['port']
KV_FILE_PATH = cfg['FileSys']['filedir'] + '/' + cfg['FileSys']['filename']