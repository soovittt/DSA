from __future__ import annotations
from typing import Generic, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class BTreeNode(Generic[T]):
    def __init__(self, t: int, leaf: bool) -> None:
        self.t = t  # minimum degree
        self.leaf = leaf
        self.keys: List[T] = []
        self.children: List["BTreeNode[T]"] = []

    def is_full(self) -> bool:
        return len(self.keys) == (2 * self.t - 1)


class BTree(Generic[T]):
    """B-Tree (minimum degree t) with search and insert (split child)."""

    def __init__(self, t: int) -> None:
        if t < 2:
            raise ValueError("t must be >= 2")
        self.t = t
        self.root = BTreeNode[T](t, True)

    def search(self, k: T) -> Optional[Tuple[BTreeNode[T], int]]:
        node = self.root
        while True:
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1
            if i < len(node.keys) and k == node.keys[i]:
                return (node, i)
            if node.leaf:
                return None
            node = node.children[i]

    def split_child(self, x: BTreeNode[T], i: int) -> None:
        t = self.t
        y = x.children[i]
        z = BTreeNode[T](t, y.leaf)
        # move top half of y to z
        z.keys = y.keys[t:]
        y.keys = y.keys[: t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys.pop())

    def insert(self, k: T) -> None:
        r = self.root
        if r.is_full():
            s = BTreeNode[T](self.t, False)
            self.root = s
            s.children.append(r)
            self.split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _insert_nonfull(self, x: BTreeNode[T], k: T) -> None:
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(k)
            i = len(x.keys) - 2
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if x.children[i].is_full():
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_nonfull(x.children[i], k)
