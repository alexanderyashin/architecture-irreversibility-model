"""
Public showcase version of stress propagation.

Defines how tension propagates across dependency edges.
This implementation is intentionally simple and illustrative.
"""

from __future__ import annotations
from typing import Dict

from src.model.system import System
from .dependency_graph import DependencyGraph


def propagation_function(tension: float, threshold: float) -> float:
    """
    Propagation function φ(T).

    Near-threshold tension propagates more strongly.
    """
    if threshold <= 0.0:
        return 0.0
    return max(0.0, tension / threshold)


def compute_propagated_tension(
    system: System,
    graph: DependencyGraph,
) -> Dict[str, float]:
    """
    Compute propagated tension for each node.
    """
    propagated: Dict[str, float] = {name: 0.0 for name in system.nodes.keys()}

    for src_name, src_node in system.nodes.items():
        for dst_name, weight in graph.neighbors(src_name):
            if dst_name not in system.nodes:
                continue

            delta = weight * propagation_function(
                src_node.tension,
                src_node.threshold,
            )
            propagated[dst_name] += delta

    return propagated
