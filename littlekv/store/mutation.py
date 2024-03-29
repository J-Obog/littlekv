from dataclasses import dataclass
from typing import List
from enum import Enum

class Operation(Enum):
    SET = "SET"
    DELETE = "DELETE"
    FLUSH = "FLUSH"

@dataclass
class Mutation:
    operation: Operation
    params: List[any]
    timestamp: int
    