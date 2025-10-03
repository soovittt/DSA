from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, List, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Entry(Generic[K, V]):
    key: K
    value: V
    tombstone: bool = False


class HashTable(Generic[K, V]):
    """Open addressing hash table with linear probing and tombstones.

    Invariants:
    - Load factor <= max_load. Resize when exceeded.
    - A tombstone indicates a deleted slot, preserving probe chains.
    - Capacity always a power of two for mask arithmetic.
    """

    _INITIAL_CAPACITY = 8

    def __init__(self, items: Optional[Iterable[Tuple[K, V]]] = None, max_load: float = 0.7) -> None:
        self._size = 0
        self._max_load = max_load
        self._capacity = HashTable._INITIAL_CAPACITY
        self._buckets: List[Optional[_Entry[K, V]]] = [None] * self._capacity
        if items is not None:
            for k, v in items:
                self.set(k, v)

    def __len__(self) -> int:
        return self._size

    def _hash(self, key: K) -> int:
        return hash(key) & 0x7FFFFFFF

    def _resize(self, new_capacity: int) -> None:
        old = self._buckets
        self._capacity = new_capacity
        self._buckets = [None] * self._capacity
        self._size = 0
        for entry in old:
            if entry is not None and not entry.tombstone:
                self.set(entry.key, entry.value)

    def _probe(self, key: K) -> int:
        mask = self._capacity - 1
        idx = self._hash(key) & mask
        first_tombstone = -1
        while True:
            slot = self._buckets[idx]
            if slot is None:
                return first_tombstone if first_tombstone != -1 else idx
            if slot.tombstone:
                if first_tombstone == -1:
                    first_tombstone = idx
            elif slot.key == key:
                return idx
            idx = (idx + 1) & mask

    def _ensure_capacity(self) -> None:
        if (self._size + 1) / self._capacity > self._max_load:
            self._resize(self._capacity * 2)

    def set(self, key: K, value: V) -> None:
        self._ensure_capacity()
        idx = self._probe(key)
        slot = self._buckets[idx]
        if slot is None or slot.tombstone:
            self._buckets[idx] = _Entry(key, value)
            self._size += 1
        else:
            slot.value = value

    def get(self, key: K) -> V:
        mask = self._capacity - 1
        idx = self._hash(key) & mask
        while True:
            slot = self._buckets[idx]
            if slot is None:
                raise KeyError(key)
            if not slot.tombstone and slot.key == key:
                return slot.value
            idx = (idx + 1) & mask

    def delete(self, key: K) -> None:
        mask = self._capacity - 1
        idx = self._hash(key) & mask
        while True:
            slot = self._buckets[idx]
            if slot is None:
                raise KeyError(key)
            if not slot.tombstone and slot.key == key:
                slot.tombstone = True
                self._size -= 1
                return
            idx = (idx + 1) & mask

    def __iter__(self) -> Iterator[Tuple[K, V]]:
        for slot in self._buckets:
            if slot is not None and not slot.tombstone:
                yield (slot.key, slot.value)
