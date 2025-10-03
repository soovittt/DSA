from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None


class BinarySearchTree(Generic[T]):
    """Binary Search Tree (unbalanced).

    Invariants:
    - For every node: left.key < node.key < right.key (strict BST invariant).
    - Inorder traversal yields sorted keys.
    """

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
        # ignore duplicates
        return node

    def insert(self, key: T) -> None:
        self._root = self._insert(self._root, key)

    def _min_node(self, node: _Node[T]) -> _Node[T]:
        while node.left is not None:
            node = node.left
        return node

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
            succ = self._min_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    def delete(self, key: T) -> None:
        self._root = self._delete(self._root, key)

    def __contains__(self, key: T) -> bool:
        node = self._root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
        return False

    def inorder(self) -> Iterator[T]:
        def traverse(n: Optional[_Node[T]]) -> Iterator[T]:
            if n is None:
                return
            yield from traverse(n.left)
            yield n.key
            yield from traverse(n.right)
        return traverse(self._root)
