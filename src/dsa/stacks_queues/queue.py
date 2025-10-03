from __future__ import annotations
from collections import deque
from typing import Deque, Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """FIFO queue with O(1) amortized enqueue/dequeue using deque.

    Invariants:
    - Front is at the left side; back is at the right side.
    - Size equals length of the deque.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._data: Deque[T] = deque()
        if values is not None:
            for v in values:
                self.enqueue(v)

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def enqueue(self, value: T) -> None:
        self._data.append(value)

    def dequeue(self) -> T:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def front(self) -> T:
        if not self._data:
            raise IndexError("queue is empty")
        return self._data[0]

    def back(self) -> T:
        if not self._data:
            raise IndexError("queue is empty")
        return self._data[-1]
