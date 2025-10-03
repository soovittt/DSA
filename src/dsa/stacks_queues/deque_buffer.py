from __future__ import annotations
from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class Deque(Generic[T]):
    """Double-ended queue using circular buffer with resizing.

    Invariants:
    - Buffer size is power of two; indices masked by capacity-1.
    - head points to first element; tail points one past last element.
    - Size tracked; buffer always has at least one empty slot.
    """

    _INITIAL_CAPACITY = 8

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._cap = Deque._INITIAL_CAPACITY
        self._mask = self._cap - 1
        self._data: List[Optional[T]] = [None] * self._cap
        self._head = 0
        self._tail = 0
        self._size = 0
        if values is not None:
            for v in values:
                self.push_back(v)

    def __len__(self) -> int:
        return self._size

    def _grow(self) -> None:
        old = self._data
        new_cap = self._cap * 2
        new: List[Optional[T]] = [None] * new_cap
        i = 0
        while self._size:
            new[i] = self.pop_front()
            i += 1
        self._data = new
        self._cap = new_cap
        self._mask = new_cap - 1
        self._head = 0
        self._tail = i
        self._size = i

    def is_empty(self) -> bool:
        return self._size == 0

    def push_front(self, value: T) -> None:
        if self._size == self._cap - 1:
            self._grow()
        self._head = (self._head - 1) & self._mask
        self._data[self._head] = value
        self._size += 1

    def push_back(self, value: T) -> None:
        if self._size == self._cap - 1:
            self._grow()
        self._data[self._tail] = value
        self._tail = (self._tail + 1) & self._mask
        self._size += 1

    def pop_front(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty deque")
        v = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) & self._mask
        self._size -= 1
        return v  # type: ignore

    def pop_back(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty deque")
        self._tail = (self._tail - 1) & self._mask
        v = self._data[self._tail]
        self._data[self._tail] = None
        self._size -= 1
        return v  # type: ignore

    def front(self) -> T:
        if self._size == 0:
            raise IndexError("deque is empty")
        return self._data[self._head]  # type: ignore

    def back(self) -> T:
        if self._size == 0:
            raise IndexError("deque is empty")
        return self._data[(self._tail - 1) & self._mask]  # type: ignore
