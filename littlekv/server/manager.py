from littlekv.store import Store
from typing import Callable, Dict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()
        self._map_lock = Lock()
        self._store_lock = Lock()
        self._pool = ThreadPoolExecutor()

    def _r_locked(self, func: Callable):
        def wraps(*args, **kwargs):
            with self._map_lock:
                return func(*args, **kwargs)
        return wraps

    def _write(self, snapshot: Dict[str,str]):
        with self._store_lock:
            self._store.write(snapshot)

    def _w_locked(self, func: Callable):
        def wraps(*args, **kwargs):
            with self._map_lock:
                func(*args, **kwargs)
                self._pool.submit(self._write, dict(self._hash_map))
        return wraps

    @_r_locked
    def get(self, key: str) -> str:
        return self._hash_map.get(key, None)

    @_r_locked
    def get_all(self) -> Dict[str,str]:
        return dict(self._hash_map)

    @_w_locked
    def set(self, key: str, value: str):
        self._hash_map[key] = value

    @_w_locked
    def delete(self, key: str):
        self._hash_map.pop(key)

    @_w_locked
    def delete_all(self):
        self._hash_map = dict()