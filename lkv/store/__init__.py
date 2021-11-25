from typing import Dict, Optional
import toml

class KVStore:
    def __init__(self, path = None) -> None:
        self.fp: str = path
        self.kv: Dict[str, str] = {}
        
        if path: 
            self._kvs_to_dict()

    def _dict_to_kvs(self) -> None:
        with open(self.fp, 'w') as f:
            f.write(toml.dumps(self.kv))
                
    def _kvs_to_dict(self) -> None:
        with open(self.fp, 'r') as f:
            self.kv = toml.loads(f.read())

    def init_store(self, path) -> None:
        self.fp = path
        self._kvs_to_dict()

    def getk(self, key) -> Optional[str]:
        return self.kv.get(key, None)

    def setk(self, key, val) -> int:
        self.kv[key] = val
        self._dict_to_kvs()
        return 1

    def delk(self, key) -> int:
        if self.getk(key) != None:
            self.kv.pop(key) 
            self._dict_to_kvs()
            return 1
        return 0

    def countk(self) -> int:
        return len(self.kv.keys())