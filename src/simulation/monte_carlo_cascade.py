"""
Public showcase version of Monte Carlo simulation with cascades.

Demonstrates how dependency-driven propagation amplifies irreversible risk.
"""

from __future__ import annotations
from typing import Callable, Dict

from src.model.system import System
from src.graph.dependency_graph import DependencyGraph
from src.graph.propagation import compute_propagated_tension


def run_cascade(
    system: System,
    graph: DependencyGraph,
    steps: int,
) -> Dict[str, float]:
    """
    Run a single cascade-aware trajectory.
    """

    for _ in range(steps):
        system.step()

        propagated = compute_propagated_tension(system, graph)
        for name, delta in propagated.items():
            system.nodes[name].tension += delta

    crossed_nodes = system.crossed_nodes()
    loss = system.expected_loss()

    return {
        "crossed": len(crossed_nodes) > 0,
        "crossed_nodes": len(crossed_nodes),
        "loss": loss,
    }


def monte_carlo_cascade(
    system_factory: Callable[[], System],
    graph_factory: Callable[[], DependencyGraph],
    steps: int,
    runs: int,
) -> Dict[str, float]:
    """
    Monte Carlo estimation with cascade propagation.
    """

    crosses = 0
    total_loss = 0.0
    total_crossed_nodes = 0

    for _ in range(runs):
        system = system_factory()
        graph = graph_factory()

        result = run_cascade(system, graph, steps)

        if result["crossed"]:
            crosses += 1

        total_loss += result["loss"]
        total_crossed_nodes += result["crossed_nodes"]

    return {
        "p_any_cross": crosses / runs,
        "expected_loss": total_loss / runs,
        "avg_crossed_nodes": total_crossed_nodes / runs,
    }
