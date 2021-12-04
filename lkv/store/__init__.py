from typing import Dict, Optional, Union
import os
import toml

class KVStore:
    def __init__(self, path: str, filename: str):
        self.__basepath: str = path
        self.__filepath: str = os.path.join(self.__basepath, filename)
        self.__kv: Dict[str, str] = {}

        if not os.path.exists(self.__basepath): 
            os.mkdir(self.__basepath)

        if not os.path.exists(self.__filepath):
            open(self.__filepath, 'w+').close()
        else:
            self.__read_keys()

    """ Storage interface """
    def __read_keys(self):
        with open(self.__filepath, 'r') as kvfile:
            self.__kv = toml.loads(kvfile.read())

    def __write_keys(self):
        with open(self.__filepath, 'w') as kvfile:
            kvfile.write(toml.dumps(self.__kv))

    """ API """
    def getk(self, key = None) -> Union[Optional[str], Dict[str, str]]:
        return self.__kv.get(key, None) if key else list(self.__kv.keys())

    def setk(self, key, val):
        self.__kv[key] = val
        self.__write_keys()

    def delk(self, key):
        if self.getk(key) != None:
            self.__kv.pop(key) 
            self.__write_keys()

    def countk(self) -> int:
        return len(self.__kv.keys())

    def cleark(self):
        self.__kv.clear()
        self.__write_keys()