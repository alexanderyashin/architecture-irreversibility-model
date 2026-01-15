"""
Public showcase version of Monte Carlo simulation (no cascades).

Estimates probability of irreversible transitions and expected loss
for a synthetic system.
"""

from __future__ import annotations
from typing import Callable, Dict

from src.model.system import System
from src.model.dynamics import clone_and_run


def monte_carlo(
    system_factory: Callable[[], System],
    steps: int,
    runs: int,
) -> Dict[str, float]:
    """
    Run Monte Carlo simulation over multiple independent trajectories.

    Parameters
    ----------
    system_factory : callable
        Factory returning a fresh System instance.
    steps : int
        Simulation horizon.
    runs : int
        Number of Monte Carlo runs.

    Returns
    -------
    dict with keys:
        - p_any_cross
        - expected_loss
        - avg_crossed_nodes
    """

    crosses = 0
    total_loss = 0.0
    total_crossed_nodes = 0

    for _ in range(runs):
        result = clone_and_run(
            system_factory=system_factory,
            steps=steps,
        )

        if result.crossed:
            crosses += 1

        total_loss += result.loss
        total_crossed_nodes += result.crossed_nodes

    return {
        "p_any_cross": crosses / runs,
        "expected_loss": total_loss / runs,
        "avg_crossed_nodes": total_crossed_nodes / runs,
    }
