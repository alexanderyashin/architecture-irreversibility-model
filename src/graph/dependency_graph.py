"""
Public showcase version of the dependency graph.

Defines a directed, weighted graph describing how stress propagates
between subsystems. This version is intentionally minimal and generic.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, Tuple

import networkx as nx


@dataclass
class DependencyGraph:
    """
    Directed weighted dependency graph.

    Nodes are identified by string keys.
    Edge weight represents relative stress propagation strength.
    """

    graph: nx.DiGraph = field(default_factory=nx.DiGraph)

    def add_node(self, name: str) -> None:
        self.graph.add_node(name)

    def add_edge(self, src: str, dst: str, weight: float) -> None:
        if weight < 0.0:
            raise ValueError("Edge weight must be non-negative")
        self.graph.add_edge(src, dst, weight=weight)

    def neighbors(self, src: str) -> Iterable[Tuple[str, float]]:
        """
        Outgoing neighbors of src as (dst, weight).
        """
        for _, dst, data in self.graph.out_edges(src, data=True):
            yield dst, data.get("weight", 0.0)

    def nodes(self) -> Iterable[str]:
        return self.graph.nodes

    def edges(self) -> Iterable[Tuple[str, str, float]]:
        for src, dst, data in self.graph.edges(data=True):
            yield src, dst, data.get("weight", 0.0)

    def __repr__(self) -> str:
        lines = ["DependencyGraph:"]
        for src, dst, w in self.edges():
            lines.append(f"  {src} -> {dst} (w={w})")
        return "\n".join(lines)
