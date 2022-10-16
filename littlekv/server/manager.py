from littlekv.store import Store
from typing import Dict

class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()

    def get(self, key: str) -> str:
        return self._hash_map.get(key, None)

    def get_all(self) -> Dict[str,str]:
        return dict(self._hash_map)

    def set(self, key: str, value: str):
        self._hash_map[key] = value

    def delete(self, key: str):
        self._hash_map.pop(key)

    def delete_all(self):
        self._hash_map = dict()