from ast import arg
from typing import List, Dict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from littlekv.store.entry import MutationEntry, Operation
from littlekv.store.store import Store

def map_from_entries(entries: List[MutationEntry]) -> Dict[str,str]:
    hash_map = dict()
    sorted_entries = sorted(entries, key=lambda entry: entry.timestamp)
    
    for entry in sorted_entries:
        op = entry.operation
        args = entry.params 

        if op == Operation.SET:
            key = args[0]
            val = args[1]
            hash_map[key] = val
        elif op == Operation.DELETE:
            key = args[0] 
            hash_map.pop(key)
        elif op == Operation.FLUSH:
            hash_map.clear()
    
    return hash_map


class LittleKVManager:
    def __init__(self, store: Store, write_async=True):
        self._store = store
        self._write_async = write_async
        self._hash_map = map_from_entries(store.read())
        self._map_lock = Lock()
        self._store_lock = Lock()
        self._pool = ThreadPoolExecutor()

    def _init_map(self):
        pass       

    def _write(self, data: Dict[str,str]):
        with self._store_lock:
            self._store.write(data)

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