from __future__ import annotations
from heapq import heappush, heappop
from typing import Dict, Hashable, Iterable, List, Tuple

Node = Hashable
Graph = Dict[Node, List[Tuple[Node, float]]]


def dijkstra(graph: Graph, source: Node) -> Dict[Node, float]:
    """Single-source shortest paths on non-negative weighted graphs.

    Invariant: when a node is popped from PQ, its distance is finalized.
    """
    dist: Dict[Node, float] = {source: 0.0}
    pq: List[Tuple[float, Node]] = [(0.0, source)]
    while pq:
        d, u = heappop(pq)
        if d != dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist
