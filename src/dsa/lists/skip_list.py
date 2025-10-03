from __future__ import annotations
import random
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    def __init__(self, key: Optional[T], level: int) -> None:
        self.key = key
        self.forward: List[Optional["_Node[T]"]] = [None] * (level + 1)


class SkipList(Generic[T]):
    """Probabilistic ordered set/map using multiple forward levels.

    Invariants:
    - Levels form towers; higher levels skip more nodes.
    - On average, search/insert/delete are O(log n).
    """

    def __init__(self, max_level: int = 16, p: float = 0.5) -> None:
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.header = _Node[T](None, max_level)

    def _random_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, key: T) -> bool:
        cur = self.header
        for i in reversed(range(self.level + 1)):
            while cur.forward[i] is not None and cur.forward[i].key < key:
                cur = cur.forward[i]  # type: ignore
        cur = cur.forward[0]  # type: ignore
        return cur is not None and cur.key == key

    def insert(self, key: T) -> None:
        update: List[_Node[T]] = [self.header] * (self.max_level + 1)
        cur = self.header
        for i in reversed(range(self.level + 1)):
            while cur.forward[i] is not None and cur.forward[i].key < key:
                cur = cur.forward[i]  # type: ignore
            update[i] = cur
        cur = cur.forward[0]  # type: ignore
        if cur is not None and cur.key == key:
            return
        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl
        node = _Node[T](key, lvl)
        for i in range(lvl + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def delete(self, key: T) -> bool:
        update: List[_Node[T]] = [self.header] * (self.max_level + 1)
        cur = self.header
        for i in reversed(range(self.level + 1)):
            while cur.forward[i] is not None and cur.forward[i].key < key:
                cur = cur.forward[i]  # type: ignore
            update[i] = cur
        cur = cur.forward[0]  # type: ignore
        if cur is None or cur.key != key:
            return False
        for i in range(self.level + 1):
            if update[i].forward[i] is not cur:
                continue
            update[i].forward[i] = cur.forward[i]
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1
        return True
