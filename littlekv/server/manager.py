from littlekv.store import Store
from typing import Dict
from threading import Lock

class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()
        self._map_lock = Lock()

    def get(self, key: str) -> str:
        with self._map_lock:
            return self._hash_map.get(key, None)

    def get_all(self) -> Dict[str,str]:
        with self._map_lock:
            return dict(self._hash_map)

    def set(self, key: str, value: str):
        with self._map_lock:
            self._hash_map[key] = value

    def delete(self, key: str):
        with self._map_lock:
            self._hash_map.pop(key)

    def delete_all(self):
        self._hash_map = dict()