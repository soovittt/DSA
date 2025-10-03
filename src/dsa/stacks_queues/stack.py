from __future__ import annotations
from typing import Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """LIFO stack with amortized O(1) push/pop using Python list as dynamic array.

    Invariants:
    - Top of stack is at the end of the underlying list.
    - Size equals length of the list.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._data: List[T] = []
        if values is not None:
            for v in values:
                self.push(v)

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]
