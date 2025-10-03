from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterable, Iterator

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
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


def _splay(root: Optional[_Node[T]], key: T) -> Optional[_Node[T]]:
    if root is None or root.key == key:
        return root
    if key < root.key:
        if root.left is None:
            return root
        if key < root.left.key:
            root.left.left = _splay(root.left.left, key)
            root = _rotate_right(root)
        elif key > root.left.key:
            root.left.right = _splay(root.left.right, key)
            if root.left.right is not None:
                root.left = _rotate_left(root.left)
        return root if root.left is None else _rotate_right(root)
    else:
        if root.right is None:
            return root
        if key > root.right.key:
            root.right.right = _splay(root.right.right, key)
            root = _rotate_left(root)
        elif key < root.right.key:
            root.right.left = _splay(root.right.left, key)
            if root.right.left is not None:
                root.right = _rotate_right(root.right)
        return root if root.right is None else _rotate_left(root)


class SplayTree(Generic[T]):
    """Splay tree with search/insert splaying accessed node to root."""

    def __init__(self, keys: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if keys is not None:
            for k in keys:
                self.insert(k)

    def search(self, key: T) -> bool:
        self._root = _splay(self._root, key)
        return self._root is not None and self._root.key == key

    def insert(self, key: T) -> None:
        if self._root is None:
            self._root = _Node(key)
            return
        self._root = _splay(self._root, key)
        if self._root.key == key:
            return
        node = _Node(key)
        if key < self._root.key:
            node.right = self._root
            node.left = self._root.left
            self._root.left = None
        else:
            node.left = self._root
            node.right = self._root.right
            self._root.right = None
        self._root = node

    def inorder(self) -> Iterator[T]:
        def traverse(n: Optional[_Node[T]]) -> Iterator[T]:
            if n is None:
                return
            yield from traverse(n.left)
            yield n.key
            yield from traverse(n.right)
        return traverse(self._root)
