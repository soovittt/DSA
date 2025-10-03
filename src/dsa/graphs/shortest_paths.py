from __future__ import annotations
from typing import Dict, Hashable, List, Tuple

Node = Hashable
Graph = Dict[Node, List[Tuple[Node, float]]]


def bellman_ford(graph: Graph, source: Node) -> Tuple[Dict[Node, float], bool]:
    """Returns (dist, has_negative_cycle_reachable).
    Graph may have negative weights; detect negative cycles reachable from source.
    """
    dist: Dict[Node, float] = {source: 0.0}
    nodes = list(graph.keys())
    for _ in range(len(nodes) - 1):
        updated = False
        for u in nodes:
            du = dist.get(u, float("inf"))
            for v, w in graph.get(u, []):
                if du + w < dist.get(v, float("inf")):
                    dist[v] = du + w
                    updated = True
        if not updated:
            break
    # detect cycle
    for u in nodes:
        du = dist.get(u, float("inf"))
        for v, w in graph.get(u, []):
            if du + w < dist.get(v, float("inf")):
                return dist, True
    return dist, False


def floyd_warshall(nodes: List[Node], graph: Graph) -> Dict[Node, Dict[Node, float]]:
    dist: Dict[Node, Dict[Node, float]] = {u: {v: float("inf") for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0.0
        for v, w in graph.get(u, []):
            dist[u][v] = min(dist[u][v], w)
    for k in nodes:
        for i in nodes:
            dik = dist[i][k]
            if dik == float("inf"):
                continue
            for j in nodes:
                alt = dik + dist[k][j]
                if alt < dist[i][j]:
                    dist[i][j] = alt
    return dist
