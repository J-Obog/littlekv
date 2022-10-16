from littlekv.store import Store
from typing import Callable, Dict
from threading import Lock

class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()
        self._map_lock = Lock()

    def r_locked(self, func: Callable):
        def wraps(*args, **kwargs):
            with self._map_lock:
                return func(*args, **kwargs)
        return wraps

    def w_locked(self, func: Callable):
        def wraps(*args, **kwargs):
            with self._map_lock:
                func(*args, **kwargs)
                self._store.write(dict(self._hash_map))
        return wraps

    @r_locked
    def get(self, key: str) -> str:
        return self._hash_map.get(key, None)

    @r_locked
    def get_all(self) -> Dict[str,str]:
        return dict(self._hash_map)

    @w_locked
    def set(self, key: str, value: str):
        self._hash_map[key] = value

    @w_locked
    def delete(self, key: str):
        self._hash_map.pop(key)

    @w_locked
    def delete_all(self):
        self._hash_map = dict()