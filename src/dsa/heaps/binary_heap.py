from __future__ import annotations
from typing import Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")


class BinaryHeap(Generic[T]):
    """Binary heap (min-heap by default) using array representation.

    Invariants:
    - For min-heap: parent <= children for all nodes.
    - Shape: complete binary tree (array packed left-to-right).
    """

    def __init__(self, values: Optional[Iterable[T]] = None, *, is_min_heap: bool = True) -> None:
        self._data: List[T] = []
        self._cmp = (lambda a, b: a <= b) if is_min_heap else (lambda a, b: a >= b)
        if values is not None:
            for v in values:
                self.push(v)

    def __len__(self) -> int:
        return len(self._data)

    def _parent(self, i: int) -> int: return (i - 1) // 2
    def _left(self, i: int) -> int: return 2 * i + 1
    def _right(self, i: int) -> int: return 2 * i + 2

    def _sift_up(self, i: int) -> None:
        while i > 0 and not self._cmp(self._data[self._parent(i)], self._data[i]):
            p = self._parent(i)
            self._data[p], self._data[i] = self._data[i], self._data[p]
            i = p

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            l = self._left(i)
            r = self._right(i)
            best = i
            if l < n and not self._cmp(self._data[best], self._data[l]):
                best = l
            if r < n and not self._cmp(self._data[best], self._data[r]):
                best = r
            if best == i:
                break
            self._data[i], self._data[best] = self._data[best], self._data[i]
            i = best

    def peek(self) -> T:
        if not self._data:
            raise IndexError("heap is empty")
        return self._data[0]

    def push(self, value: T) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def heapify(self, values: Iterable[T]) -> None:
        self._data = list(values)
        for i in reversed(range(len(self._data) // 2)):
            self._sift_down(i)
