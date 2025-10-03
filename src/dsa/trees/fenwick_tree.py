from __future__ import annotations
from typing import List


class FenwickTree:
    """Fenwick (Binary Indexed) Tree for prefix sums.

    Invariant: tree[i] stores sum over range (i - lsb(i) + 1 .. i).
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.tree: List[int] = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        i = idx + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, idx: int) -> int:
        s = 0
        i = idx + 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
