from __future__ import annotations
from typing import Dict, Hashable, Iterable, List, Tuple
from heapq import heappush, heappop

from ..union_find.union_find import UnionFind

Node = Hashable
Edge = Tuple[Node, Node, float]
Graph = Dict[Node, List[Tuple[Node, float]]]


def kruskal_mst(vertices: Iterable[Node], edges: Iterable[Edge]) -> Tuple[float, List[Edge]]:
    uf = UnionFind(vertices)
    total = 0.0
    mst: List[Edge] = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
    return total, mst


def prim_mst(graph: Graph, start: Node) -> Tuple[float, List[Edge]]:
    total = 0.0
    mst: List[Edge] = []
    visited = set([start])
    pq: List[Tuple[float, Node, Node]] = []  # (w, u, v)
    for v, w in graph.get(start, []):
        heappush(pq, (w, start, v))
    while pq and len(visited) < len(graph):
        w, u, v = heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        total += w
        for x, wx in graph.get(v, []):
            if x not in visited:
                heappush(pq, (wx, v, x))
    return total, mst
