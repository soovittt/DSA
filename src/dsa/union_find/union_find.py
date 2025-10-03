from __future__ import annotations
from typing import Dict, Generic, Iterable, TypeVar

T = TypeVar("T")


class UnionFind(Generic[T]):
    """Disjoint Set Union (Union-Find) with union by rank and path compression.

    Invariants:
    - parent[x] is representative parent; rank approximates tree height.
    - find(x) flattens tree via path compression.
    - union(x, y) attaches smaller rank tree under larger rank.
    """

    def __init__(self, items: Iterable[T]) -> None:
        self.parent: Dict[T, T] = {}
        self.rank: Dict[T, int] = {}
        for x in items:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x: T) -> T:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: T, b: T) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
