"""
Runnable cascade demo for the Architecture Irreversibility Model.

This script demonstrates dependency-driven amplification of risk
using fully synthetic parameters.
"""

from src.model.node import Node
from src.model.system import System
from src.graph.dependency_graph import DependencyGraph
from src.simulation.monte_carlo_cascade import monte_carlo_cascade


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

    system.add_node(
        Node(
            name="DeliveryProcess",
            threshold=1.0,
            forcing=0.5,
            capacity=0.45,
            coherence=0.85,
            noise_sigma=0.05,
            impact=300_000.0,
        )
    )

    return system


def graph_factory() -> DependencyGraph:
    graph = DependencyGraph()

    graph.add_node("CorePlatform")
    graph.add_node("IntegrationLayer")
    graph.add_node("DeliveryProcess")

    # Directed dependencies (synthetic)
    graph.add_edge("CorePlatform", "IntegrationLayer", weight=0.6)
    graph.add_edge("IntegrationLayer", "DeliveryProcess", weight=0.4)

    return graph


if __name__ == "__main__":
    result = monte_carlo_cascade(
        system_factory=system_factory,
        graph_factory=graph_factory,
        steps=50,
        runs=5_000,
    )

    print("Monte Carlo result (public demo, with cascades):")
    for k, v in result.items():
        print(f"  {k}: {v}")
