from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterable

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None
    size: int = 1  # size of subtree rooted at node


def _size(n: Optional[_Node[T]]) -> int:
    return n.size if n is not None else 0


def _update(n: _Node[T]) -> None:
    n.size = 1 + _size(n.left) + _size(n.right)


class OrderStatisticsTree(Generic[T]):
    """BST augmented with subtree sizes to support select and rank.

    - select(k): kth (0-indexed) smallest key
    - rank(x): number of keys < x
    """

    def __init__(self, keys: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if keys is not None:
            for k in keys:
                self.insert(k)

    def _insert(self, n: Optional[_Node[T]], key: T) -> _Node[T]:
        if n is None:
            return _Node(key)
        if key < n.key:
            n.left = self._insert(n.left, key)
        elif key > n.key:
            n.right = self._insert(n.right, key)
        _update(n)
        return n

    def insert(self, key: T) -> None:
        self._root = self._insert(self._root, key)

    def select(self, k: int) -> T:
        n = self._root
        while n is not None:
            left_size = _size(n.left)
            if k < left_size:
                n = n.left
            elif k == left_size:
                return n.key
            else:
                k -= left_size + 1
                n = n.right
        raise IndexError("k out of range")

    def rank(self, key: T) -> int:
        n = self._root
        r = 0
        while n is not None:
            if key <= n.key:
                n = n.left
            else:
                r += 1 + _size(n.left)
                n = n.right
        return r
