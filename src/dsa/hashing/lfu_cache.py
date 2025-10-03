from __future__ import annotations
from collections import OrderedDict
from typing import Dict, Generic, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class LFUCache(Generic[K, V]):
    """LFU Cache with O(1) get/put using frequency buckets.

    Invariants:
    - key_to_val_freq maps key -> (value, freq)
    - freq_to_keys maps freq -> OrderedDict of keys for LRU among same freq
    - min_freq tracks current minimum frequency in cache
    """

    def __init__(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("capacity must be >= 0")
        self.capacity = capacity
        self.size = 0
        self.key_to_val_freq: Dict[K, Tuple[V, int]] = {}
        self.freq_to_keys: Dict[int, OrderedDict[K, None]] = {}
        self.min_freq = 0

    def _touch(self, key: K, value: Optional[V] = None) -> None:
        val, freq = self.key_to_val_freq[key]
        if value is not None:
            val = value
        # remove from current freq bucket
        bucket = self.freq_to_keys[freq]
        bucket.pop(key, None)
        if not bucket:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        # add to next freq bucket
        new_freq = freq + 1
        self.freq_to_keys.setdefault(new_freq, OrderedDict())[key] = None
        self.key_to_val_freq[key] = (val, new_freq)

    def get(self, key: K) -> Optional[V]:
        if key not in self.key_to_val_freq:
            return None
        val, _ = self.key_to_val_freq[key]
        self._touch(key)
        return val

    def put(self, key: K, value: V) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            # update value and bump freq
            self._touch(key, value)
            return
        if self.size == self.capacity:
            # evict LRU from min_freq bucket
            bucket = self.freq_to_keys[self.min_freq]
            evict_key, _ = bucket.popitem(last=False)
            if not bucket:
                del self.freq_to_keys[self.min_freq]
            del self.key_to_val_freq[evict_key]
            self.size -= 1
        # insert new key with freq 1
        self.freq_to_keys.setdefault(1, OrderedDict())[key] = None
        self.key_to_val_freq[key] = (value, 1)
        self.min_freq = 1
        self.size += 1
