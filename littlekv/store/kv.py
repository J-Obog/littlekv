from abc import ABC, abstractmethod
from typing import Dict

class KeyValueStore(ABC):
    @abstractmethod
    def get(self, key: str) -> str:
        ...
    
    @abstractmethod
    def get_all(self) -> Dict[str,str]:
        ... 
    
    @abstractmethod
    def set(self, key: str, value: str):
        ...

    @abstractmethod
    def delete(self, key: str):
        ...
        
    @abstractmethod
    def delete_all(self):
        ...