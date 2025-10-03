from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    key: T
    red: bool = True  # True = red, False = black
    left: Optional["_Node[T]"] = None
    right: Optional["_Node[T]"] = None
    parent: Optional["_Node[T]"] = None


class RedBlackTree(Generic[T]):
    """Red-Black Tree with insert + fixup (CLRS-style).

    Invariants:
    - Each node is red or black; root is black.
    - Red node has black children; every path has same number of black nodes.
    """

    def __init__(self, keys: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_Node[T]] = None
        if keys is not None:
            for k in keys:
                self.insert(k)

    def _is_red(self, x: Optional[_Node[T]]) -> bool:
        return bool(x and x.red)

    def _left_rotate(self, x: _Node[T]) -> None:
        y = x.right
        assert y is not None
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self._root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: _Node[T]) -> None:
        x = y.left
        assert x is not None
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self._root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key: T) -> None:
        # BST insert
        parent: Optional[_Node[T]] = None
        cur = self._root
        while cur is not None:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return  # ignore duplicates
        z = _Node(key=key, red=True, parent=parent)
        if parent is None:
            self._root = z
        elif key < parent.key:
            parent.left = z
        else:
            parent.right = z
        # fixup
        self._insert_fixup(z)

    def _insert_fixup(self, z: _Node[T]) -> None:
        while self._is_red(z.parent):
            gp = z.parent.parent
            if z.parent is gp.left:  # type: ignore
                y = gp.right  # uncle  # type: ignore
                if self._is_red(y):
                    z.parent.red = False
                    y.red = False  # type: ignore
                    gp.red = True  # type: ignore
                    z = gp  # type: ignore
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.red = False
                    gp.red = True  # type: ignore
                    self._right_rotate(gp)  # type: ignore
            else:
                y = gp.left  # type: ignore
                if self._is_red(y):
                    z.parent.red = False
                    y.red = False  # type: ignore
                    gp.red = True  # type: ignore
                    z = gp  # type: ignore
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.red = False
                    gp.red = True  # type: ignore
                    self._left_rotate(gp)  # type: ignore
        if self._root is not None:
            self._root.red = False

    def inorder(self) -> Iterator[T]:
        def traverse(n: Optional[_Node[T]]) -> Iterator[T]:
            if n is None:
                return
            yield from traverse(n.left)
            yield n.key
            yield from traverse(n.right)
        return traverse(self._root)
