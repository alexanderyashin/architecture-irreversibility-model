"""
Public showcase version of the Node model.

This implementation demonstrates the mechanics of tension accumulation
and irreversible threshold crossing. It contains no operational or
calibration-specific logic.
"""

from __future__ import annotations
from dataclasses import dataclass
import random


@dataclass
class Node:
    """
    A bounded subsystem that accumulates tension and may cross
    an irreversible threshold.
    """

    name: str

    # State
    tension: float = 0.0

    # Parameters (synthetic / illustrative)
    threshold: float = 1.0          # irreversibility threshold
    forcing: float = 0.0            # external load
    capacity: float = 0.0           # compensation capacity
    coherence: float = 1.0           # internal stabilizing factor (0..1)
    noise_sigma: float = 0.0         # stochastic disturbance scale

    # Economic impact proxy (synthetic)
    impact: float = 0.0

    def step(self) -> None:
        """
        Advance node state by one time step.

        T(t+1) = max(0, T(t) + F - K + ε)
        where ε ~ N(0, σ)
        """

        noise = random.gauss(0.0, self.noise_sigma) if self.noise_sigma > 0.0 else 0.0
        delta = self.forcing - self.capacity + noise

        # coherence attenuates effective stress
        delta *= max(0.0, min(1.0, self.coherence))

        self.tension = max(0.0, self.tension + delta)

    def crossed_threshold(self) -> bool:
        """
        Check whether the node has crossed the irreversibility threshold.
        """
        return self.tension >= self.threshold

    def reset(self) -> None:
        """
        Reset node tension.
        """
        self.tension = 0.0

    def __repr__(self) -> str:
        status = "IRREVERSIBLE" if self.crossed_threshold() else "stable"
        return (
            f"Node(name={self.name}, "
            f"tension={self.tension:.3f}, "
            f"threshold={self.threshold}, "
            f"status={status})"
        )
