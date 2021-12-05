from typing import Dict, Optional, Union
import os
import toml
import gzip

class KVStore:
    def __init__(self, path: str, filename: str):
        self.__fp: str = os.path.join(path, filename)
        self.__kv: Dict[str, any] = {}

        if not os.path.exists(path):
            os.mkdir(path)

        if not os.path.exists(self.__fp):
            open(self.__fp, 'wb+').close()
        else:
            self.__read_keys()

    """ Storage interface """
    def __read_keys(self):
        with open(self.__fp, 'rb') as f:
            bytes_decompressed = gzip.decompress(f.read())
            content = bytes_decompressed.decode('utf-8')
            self.__kv = toml.loads(content)

    def __write_keys(self):
        with open(self.__fp, 'wb') as f:
            content = toml.dumps(self.__kv)
            bytes_compressed = gzip.compress(content.encode('utf-8'))
            f.write(bytes_compressed)

    """ API """
    def getk(self, key = None) -> Union[Optional[any], Dict[str, any]]:
        return self.__kv.get(key, None) if key else list(self.__kv.keys())

    def setk(self, key, val):
        self.__kv[key] = val
        self.__write_keys()

    def delk(self, key):
        if self.__kv.get(key, None) != None:
            self.__kv.pop(key)
            self.__write_keys()

    def countk(self) -> int:
        return len(self.__kv.keys())

    def cleark(self):
        self.__kv.clear()
        self.__write_keys()