from abc import ABC, abstractmethod
from typing import Dict

class Store(ABC):
    @abstractmethod
    def read(self) -> Dict[str,str]:
        ...

    @abstractmethod
    def write(self, data: Dict[str,str]):
        ...