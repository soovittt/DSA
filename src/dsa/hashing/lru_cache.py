from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Node(Generic[K, V]):
    key: K
    value: V
    prev: Optional["_Node[K, V]"] = None
    next: Optional["_Node[K, V]"] = None


class LRUCache(Generic[K, V]):
    """LRU Cache using hash map + doubly linked list (O(1) get/put).

    Invariants:
    - Most recently used at head.next; least at tail.prev.
    - Capacity fixed; put evicts tail when full.
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._cap = capacity
        self._map: Dict[K, _Node[K, V]] = {}
        self._head: _Node[K, V] = _Node(None, None)  # type: ignore
        self._tail: _Node[K, V] = _Node(None, None)  # type: ignore
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node[K, V]) -> None:
        node.prev.next = node.next  # type: ignore
        node.next.prev = node.prev  # type: ignore

    def _insert_at_front(self, node: _Node[K, V]) -> None:
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node  # type: ignore
        self._head.next = node

    def get(self, key: K) -> Optional[V]:
        node = self._map.get(key)
        if not node:
            return None
        self._remove(node)
        self._insert_at_front(node)
        return node.value

    def put(self, key: K, value: V) -> None:
        node = self._map.get(key)
        if node:
            node.value = value
            self._remove(node)
            self._insert_at_front(node)
            return
        if len(self._map) == self._cap:
            lru = self._tail.prev
            assert lru is not self._head
            self._remove(lru)  # type: ignore
            self._map.pop(lru.key)  # type: ignore
        new_node = _Node(key, value)
        self._insert_at_front(new_node)
        self._map[key] = new_node
