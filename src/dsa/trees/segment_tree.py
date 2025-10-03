from __future__ import annotations
from typing import Callable, List, Sequence, TypeVar

T = TypeVar("T")


class SegmentTree:
    """Segment tree for range sum (custom op supported).

    Invariants:
    - Tree size is power-of-two padded; leaves hold array values.
    - Parent stores op(left, right); op must be associative.
    """

    def __init__(self, arr: Sequence[T], *, op: Callable[[T, T], T] = lambda a, b: a + b, identity: T = 0) -> None:
        n = 1
        while n < len(arr):
            n <<= 1
        self.n = n
        self.op = op
        self.identity = identity
        self.data: List[T] = [identity] * (2 * n)
        # build
        self.data[n:n+len(arr)] = arr[:]  # type: ignore
        for i in range(n - 1, 0, -1):
            self.data[i] = op(self.data[2 * i], self.data[2 * i + 1])

    def update(self, idx: int, value: T) -> None:
        i = idx + self.n
        self.data[i] = value
        i //= 2
        while i >= 1:
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])
            i //= 2

    def query(self, l: int, r: int) -> T:
        """Query on [l, r) half-open interval."""
        res_left, res_right = self.identity, self.identity
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res_left = self.op(res_left, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res_right = self.op(self.data[r], res_right)
            l //= 2
            r //= 2
        return self.op(res_left, res_right)
