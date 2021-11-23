import toml

def parse_config():
    with open('kvs.toml', 'r') as file:
        return toml.loads(file.read())