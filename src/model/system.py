"""
Public showcase version of the System container.

Aggregates nodes and exposes system-level metrics
without any operational or commercial logic.
"""

from __future__ import annotations
from typing import Dict, List
from dataclasses import dataclass, field

from .node import Node


@dataclass
class System:
    """
    A collection of nodes evolving over a simulation horizon.
    """

    nodes: Dict[str, Node] = field(default_factory=dict)

    def add_node(self, node: Node) -> None:
        """
        Add a node to the system.
        """
        if node.name in self.nodes:
            raise ValueError(f"Node '{node.name}' already exists")
        self.nodes[node.name] = node

    def step(self) -> None:
        """
        Advance all nodes by one time step.
        """
        for node in self.nodes.values():
            node.step()

    def reset(self) -> None:
        """
        Reset all node states.
        """
        for node in self.nodes.values():
            node.reset()

    # -------------------------
    # Metrics
    # -------------------------

    def crossed_nodes(self) -> List[Node]:
        """
        Nodes that crossed irreversibility.
        """
        return [n for n in self.nodes.values() if n.crossed_threshold()]

    def any_crossed(self) -> bool:
        """
        Whether any node crossed irreversibility.
        """
        return any(n.crossed_threshold() for n in self.nodes.values())

    def expected_loss(self) -> float:
        """
        Realized loss for current state.
        """
        return sum(n.impact for n in self.crossed_nodes())

    def snapshot(self) -> Dict[str, float]:
        """
        Snapshot of node tensions.
        """
        return {name: node.tension for name, node in self.nodes.items()}

    def __repr__(self) -> str:
        lines = ["System state:"]
        for node in self.nodes.values():
            lines.append(f"  {repr(node)}")
        return "\n".join(lines)
