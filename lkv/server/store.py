import toml

class KVStore:
    def __init__(self, path):
        self.fp = path
        self.kv = {}
        self.kvs_to_dict()

    def _dict_to_kvs(self):
        with open(self.fp, 'w') as f:
            f.write(toml.dumps(self.kv))
                
    def kvs_to_dict(self):
        with open(self.fp, 'r') as f:
            self.kv = toml.loads(f.read())

    def getk(self, key):
        return self.kv.get(key, None)

    def setk(self, key, val):
        self.kv[key] = val
        self._dict_to_kvs()
        return 1

    def delk(self, key):
        if self.getk(key) != None:
            self.kv.pop(key) 
            self._dict_to_kvs()
            return 1
        return 0

    def countk(self):
        return len(self.kv.keys())