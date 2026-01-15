"""
Minimal runnable example for the Architecture Irreversibility Model.

This script runs a synthetic Monte Carlo simulation without cascades.
It is intended for demonstration and reproducibility only.
"""

from src.model.node import Node
from src.model.system import System
from src.simulation.monte_carlo import monte_carlo


def system_factory() -> System:
    system = System()

    system.add_node(
        Node(
            name="CorePlatform",
            threshold=1.0,
            forcing=0.6,
            capacity=0.3,
            coherence=0.9,
            noise_sigma=0.05,
            impact=1_000_000.0,
        )
    )

    system.add_node(
        Node(
            name="IntegrationLayer",
            threshold=1.0,
            forcing=0.4,
            capacity=0.35,
            coherence=0.8,
            noise_sigma=0.05,
            impact=500_000.0,
        )
    )

    return system


if __name__ == "__main__":
    result = monte_carlo(
        system_factory=system_factory,
        steps=50,
        runs=5_000,
    )

    print("Monte Carlo result (public demo, no cascades):")
    for k, v in result.items():
        print(f"  {k}: {v}")
