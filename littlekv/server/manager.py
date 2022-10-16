from littlekv.store import Store


class LittleKVManager:
    def __init__(self, store: Store):
        self._store = store
        self._hash_map = store.read()

    def get(self):
        pass

    def set(self):
        pass