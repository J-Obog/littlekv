import toml

CONFIG_FILE = 'config.toml'

def parse_config():
    with open(CONFIG_FILE, 'r') as file:
        return toml.loads(file.read())