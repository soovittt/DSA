from __future__ import annotations
import math
from typing import Iterable


class BloomFilter:
    """Bloom filter with k hash functions over a bit array.

    False positive, never false negative (for inserted items).
    """

    def __init__(self, n: int, p: float = 0.01) -> None:
        # m = -(n ln p) / (ln 2)^2, k = (m/n) ln 2
        m = int(-(n * math.log(p)) / (math.log(2) ** 2))
        k = max(1, int((m / n) * math.log(2)))
        self.m = m
        self.k = k
        self.bits = bytearray((m + 7) // 8)

    def _hashes(self, item: str) -> Iterable[int]:
        # Double hashing scheme using Python's built-in hash for portability
        # Generate k indices as (h1 + i*h2) mod m
        h1 = hash((item, 0)) & 0x7FFFFFFF
        h2 = (hash((item, 1)) & 0x7FFFFFFF) | 1  # ensure odd
        for i in range(self.k):
            yield (h1 + i * h2) % self.m

    def add(self, item: str) -> None:
        for h in self._hashes(item):
            self.bits[h >> 3] |= 1 << (h & 7)

    def __contains__(self, item: str) -> bool:
        for h in self._hashes(item):
            if not (self.bits[h >> 3] & (1 << (h & 7))):
                return False
        return True
