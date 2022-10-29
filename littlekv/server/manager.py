import time
from typing import List, Dict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from littlekv.store.mutation import Mutation, Operation
from littlekv.store.store import Store


def map_from_entries(entries: List[Mutation]) -> Dict[str,str]:
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
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = map_from_entries(store.read())
        self._pool = ThreadPoolExecutor()
        self._map_lock = Lock()
        self._store_lock = Lock()

    def _save(self, op: Operation, args: List[any]):
        with self._store_lock:
            now = int(time.time())
            self._store.write(Mutation(op, args, now))

    def get(self, key: str) -> str:
        with self._map_lock:
            return self._hash_map.get(key, None)

    def set(self, key: str, value: str):
        with self._map_lock:
            self._hash_map[key] = value
            self._pool.submit(self._save, Operation.SET, [key, value])

    def delete(self, key: str):
        with self._map_lock:
            self._hash_map.pop(key)
            self._pool.submit(self._save, Operation.DELETE, [key])

    def delete_all(self):
        with self._map_lock:
            self._hash_map.clear()
            self._pool.submit(self._save, Operation.FLUSH, [])