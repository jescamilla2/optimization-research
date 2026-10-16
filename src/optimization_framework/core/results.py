from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class OptimizationResult:
    """
    Results returned by the optimization algorithm
    """

    best_x: float
    best_f: float
    n_evals: int
    n_iterations: int
    history: List[Dict[str, Any]] = field(default_factory=list)