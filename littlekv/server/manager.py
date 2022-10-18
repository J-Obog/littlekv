from littlekv.store import Store
from typing import Dict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()
        self._map_lock = Lock()
        self._store_lock = Lock()
        self._pool = ThreadPoolExecutor()

    def _write(self, snapshot: Dict[str,str]):
        with self._store_lock:
            self._store.write(snapshot)

    def get(self, key: str) -> str:
        with self._map_lock:
            return self._hash_map.get(key, None)

    def get_all(self) -> Dict[str,str]:
        with self._map_lock:
            return dict(self._hash_map)

    def set(self, key: str, value: str):
        with self._map_lock:
            self._hash_map[key] = value
            self._pool.submit(self._write, dict(self._hash_map))

    def delete(self, key: str):
        with self._map_lock:
            self._hash_map.pop(key)
            self._pool.submit(self._write, dict(self._hash_map))

    def delete_all(self):
        with self._map_lock:
            self._hash_map = dict()
            self._pool.submit(self._write, dict(self._hash_map))