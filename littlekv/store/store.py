from abc import ABC, abstractmethod
from typing import List
from littlekv.store.mutation import Mutation

class Store(ABC):
    @abstractmethod
    def read(self) -> List[Mutation]:
        ...

    @abstractmethod
    def write(self, entry: Mutation):
        ...