from typing import Dict, Optional
from lkv.config import STORE_PATH
import os
import toml

class KVStore:
    def __init__(self, path: Optional[str] = None) -> None:
        self.__basepath: str = path or STORE_PATH
        self.__filepath: str = os.path.join(self.__basepath, 'dump.kv')
        self.__kv: Dict[str, str] = {}

        if not os.path.exists(self.__basepath): 
            os.mkdir(self.__basepath)

        if not os.path.exists(self.__filepath):
            open(self.__filepath, 'w+').close()
        else:
            self.__read_keys()

    """ Helpers """
    def __read_keys(self) -> None:
        with open(self.__filepath, 'r') as kvfile:
            self.__kv = toml.loads(kvfile.read())

    def __write_keys(self) -> None:
        with open(self.__filepath, 'w') as kvfile:
            kvfile.write(toml.dumps(self.__kv))

    """ API """
    def getk(self, key) -> Optional[str]:
        return self.kv.get(key, None)

    def setk(self, key, val) -> None:
        self.kv[key] = val
        self.__write_keys()

    def delk(self, key) -> None:
        if self.getk(key) != None:
            self.kv.pop(key) 
            self.__write_keys()

    def countk(self) -> int:
        return len(self.__kv.keys())