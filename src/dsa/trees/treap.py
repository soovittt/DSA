from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Generic, Optional, Tuple, TypeVar, Iterable, Iterator

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    priority: int
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None


def _rotate_right(y: _Node[T]) -> _Node[T]:
    x = y.left
    y.left = x.right  # type: ignore
    x.right = y  # type: ignore
    return x  # type: ignore


def _rotate_left(x: _Node[T]) -> _Node[T]:
    y = x.right
    x.right = y.left  # type: ignore
    y.left = x  # type: ignore
    return y  # type: ignore


class Treap(Generic[T]):
    """Randomized balanced BST (heap on priorities)."""

    def __init__(self, keys: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if keys is not None:
            for k in keys:
                self.insert(k)

    def _insert(self, node: Optional[_Node[T]], key: T) -> _Node[T]:
        if node is None:
            return _Node(key, random.randrange(1 << 31))
        if key < node.key:
            node.left = self._insert(node.left, key)
            if node.left.priority < node.priority:  # type: ignore
                node = _rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            if node.right.priority < node.priority:  # type: ignore
                node = _rotate_left(node)
        return node

    def insert(self, key: T) -> None:
        self._root = self._insert(self._root, key)

    def _delete(self, node: Optional[_Node[T]], key: T) -> Optional[_Node[T]]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            if node.left.priority < node.right.priority:
                node = _rotate_right(node)
                node.right = self._delete(node.right, key)  # type: ignore
            else:
                node = _rotate_left(node)
                node.left = self._delete(node.left, key)  # type: ignore
        return node

    def delete(self, key: T) -> None:
        self._root = self._delete(self._root, key)

    def inorder(self) -> Iterator[T]:
        def traverse(n: Optional[_Node[T]]) -> Iterator[T]:
            if n is None:
                return
            yield from traverse(n.left)
            yield n.key
            yield from traverse(n.right)
        return traverse(self._root)
