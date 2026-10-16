from dataclasses import dataclass
from typing import Callable

@dataclass
class Problem1D:
    f: Callable
    df: Callable
    a: float
    b: float
    name: str = "Unnamed Problem"

@dataclass
class ConstrainedProblem1D(Problem1D):
    g: Callable = None