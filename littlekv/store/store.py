from abc import ABC, abstractmethod
from typing import List
from littlekv.store.entry import MutationEntry

class Store(ABC):
    @abstractmethod
    def read(self) -> List[MutationEntry]:
        ...

    @abstractmethod
    def write(self, entry: MutationEntry):
        ...