from __future__ import annotations
from collections import deque
from typing import Deque, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar

T = TypeVar("T")


class Graph(Generic[T]):
    """Directed graph using adjacency list.

    Invariants:
    - Every vertex key exists in adjacency dict; missing keys imply empty adjacency.
    - No parallel edges by default; add checks if needed.
    """

    def __init__(self, edges: Optional[Iterable[Tuple[T, T]]] = None) -> None:
        self.adj: Dict[T, List[T]] = {}
        if edges is not None:
            for u, v in edges:
                self.add_edge(u, v)

    def add_vertex(self, u: T) -> None:
        if u not in self.adj:
            self.adj[u] = []

    def add_edge(self, u: T, v: T) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)

    def bfs(self, source: T) -> Iterator[T]:
        seen: Set[T] = {source}
        q: Deque[T] = deque([source])
        while q:
            u = q.popleft()
            yield u
            for w in self.adj.get(u, []):
                if w not in seen:
                    seen.add(w)
                    q.append(w)

    def dfs(self, source: T) -> Iterator[T]:
        seen: Set[T] = set()

        def visit(u: T) -> Iterator[T]:
            seen.add(u)
            yield u
            for w in self.adj.get(u, []):
                if w not in seen:
                    yield from visit(w)

        return visit(source)

    def topological_sort(self) -> List[T]:
        indeg: Dict[T, int] = {u: 0 for u in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                indeg[v] = indeg.get(v, 0) + 1
        q: Deque[T] = deque([u for u, d in indeg.items() if d == 0])
        order: List[T] = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj.get(u, []):
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(order) != len(indeg):
            raise ValueError("graph has a cycle")
        return order
