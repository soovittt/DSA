from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class DoublyNode(Generic[T]):
    value: T
    prev: Optional["DoublyNode[T]"] = None
    next: Optional["DoublyNode[T]"] = None


class DoublyLinkedList(Generic[T]):
    """Doubly linked list with sentinel head/tail for simpler edge cases.

    Invariants:
    - Sentinels head.prev is None and tail.next is None.
    - Empty: head.next is tail and tail.prev is head.
    - Size is tracked explicitly.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._head: DoublyNode[T] = DoublyNode(None)  # type: ignore
        self._tail: DoublyNode[T] = DoublyNode(None)  # type: ignore
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
        if values is not None:
            for v in values:
                self.push_back(v)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        cur = self._head.next
        while cur is not None and cur is not self._tail:
            yield cur.value
            cur = cur.next

    def _insert_between(self, value: T, left: DoublyNode[T], right: DoublyNode[T]) -> None:
        node = DoublyNode(value, prev=left, next=right)
        left.next = node
        right.prev = node
        self._size += 1

    def _remove_node(self, node: DoublyNode[T]) -> T:
        assert node is not self._head and node is not self._tail
        node.prev.next = node.next  # type: ignore
        node.next.prev = node.prev  # type: ignore
        self._size -= 1
        return node.value

    def push_front(self, value: T) -> None:
        self._insert_between(value, self._head, self._head.next)  # type: ignore

    def push_back(self, value: T) -> None:
        self._insert_between(value, self._tail.prev, self._tail)  # type: ignore

    def pop_front(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty list")
        return self._remove_node(self._head.next)  # type: ignore

    def pop_back(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty list")
        return self._remove_node(self._tail.prev)  # type: ignore

    def clear(self) -> None:
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
