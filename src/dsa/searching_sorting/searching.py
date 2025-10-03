from __future__ import annotations
from typing import Iterable, Sequence, TypeVar

T = TypeVar("T")


def linear_search(a: Iterable[T], target: T) -> int:
    """Return index of first occurrence or -1 if not found.

    Complexity: O(n) time, O(1) extra space.
    """
    for i, x in enumerate(a):
        if x == target:
            return i
    return -1


def binary_search(a: Sequence[T], target: T) -> int:
    """Return index of target in sorted `a` or -1 if not found.

    Invariant: search space is [lo, hi], inclusive.
    Complexity: O(log n) time.
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
