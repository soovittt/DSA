from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class SinglyNode(Generic[T]):
    value: T
    next: Optional["SinglyNode[T]"] = None


class SinglyLinkedList(Generic[T]):
    """Singly linked list with head/tail, O(1) push/pop front, O(1) push back.

    Invariants:
    - If list is empty, both head and tail are None and size == 0.
    - If list is non-empty, head and tail reference valid nodes and tail.next is None.
    - Size tracks the number of nodes.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._head: Optional[SinglyNode[T]] = None
        self._tail: Optional[SinglyNode[T]] = None
        self._size: int = 0
        if values is not None:
            for v in values:
                self.push_back(v)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        node = self._head
        while node is not None:
            yield node.value
            node = node.next

    def is_empty(self) -> bool:
        return self._size == 0

    def front(self) -> T:
        if self._head is None:
            raise IndexError("list is empty")
        return self._head.value

    def back(self) -> T:
        if self._tail is None:
            raise IndexError("list is empty")
        return self._tail.value

    def push_front(self, value: T) -> None:
        new_node = SinglyNode(value, self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._size += 1

    def push_back(self, value: T) -> None:
        new_node = SinglyNode(value)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("pop from empty list")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def find(self, value: T) -> Optional[SinglyNode[T]]:
        node = self._head
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        return None

    def remove_after(self, prev: Optional[SinglyNode[T]]) -> Optional[T]:
        """Remove node after `prev`. If prev is None, remove head.
        Returns removed value if any.
        """
        if prev is None:
            if self._head is None:
                return None
            return self.pop_front()
        target = prev.next
        if target is None:
            return None
        prev.next = target.next
        if target is self._tail:
            self._tail = prev
        self._size -= 1
        return target.value
