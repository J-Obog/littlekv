import toml

CONFIG_FILE = 'lkv.config'

def parse_config():
    with open(CONFIG_FILE, 'r') as file:
        return toml.loads(file.read())