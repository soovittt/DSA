from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterable, Iterator

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None
    height: int = 1


def _h(n: Optional[_Node[T]]) -> int:
    return n.height if n is not None else 0


def _update(n: _Node[T]) -> None:
    n.height = 1 + max(_h(n.left), _h(n.right))


def _bf(n: _Node[T]) -> int:
    return _h(n.left) - _h(n.right)


def _rotate_right(y: _Node[T]) -> _Node[T]:
    x = y.left
    T2 = x.right  # type: ignore
    x.right = y  # type: ignore
    y.left = T2
    _update(y)
    _update(x)  # type: ignore
    return x  # type: ignore


def _rotate_left(x: _Node[T]) -> _Node[T]:
    y = x.right
    T2 = y.left  # type: ignore
    y.left = x  # type: ignore
    x.right = T2
    _update(x)
    _update(y)  # type: ignore
    return y  # type: ignore


class AVLTree(Generic[T]):
    """AVL self-balancing BST (insert + rotations)."""

    def __init__(self, keys: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if keys is not None:
            for k in keys:
                self.insert(k)

    def _insert(self, node: Optional[_Node[T]], key: T) -> _Node[T]:
        if node is None:
            return _Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        _update(node)
        balance = _bf(node)
        if balance > 1:
            if key > node.left.key:  # type: ignore
                node.left = _rotate_left(node.left)  # type: ignore
            return _rotate_right(node)
        if balance < -1:
            if key < node.right.key:  # type: ignore
                node.right = _rotate_right(node.right)  # type: ignore
            return _rotate_left(node)
        return node

    def insert(self, key: T) -> None:
        self._root = self._insert(self._root, key)

    def inorder(self) -> Iterator[T]:
        def traverse(n: Optional[_Node[T]]) -> Iterator[T]:
            if n is None:
                return
            yield from traverse(n.left)
            yield n.key
            yield from traverse(n.right)
        return traverse(self._root)
