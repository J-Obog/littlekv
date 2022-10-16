from abc import ABC, abstractmethod

class PersistentStore(ABC):
    @abstractmethod
    def read(self) -> str:
        ...

    @abstractmethod
    def write(self, data: str):
        ...