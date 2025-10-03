from __future__ import annotations
from typing import Callable, List, MutableSequence, TypeVar

T = TypeVar("T")


def _default_cmp(a: T, b: T) -> bool:  # True if a <= b
    return a <= b


def insertion_sort(a: MutableSequence[T], *, cmp: Callable[[T, T], bool] = _default_cmp) -> None:
    """Stable, in-place O(n^2) worst-case; good for small arrays.
    Invariant: a[0..i) is sorted before each outer iteration.
    """
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and not cmp(a[j], x):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


def merge_sort(a: MutableSequence[T], *, cmp: Callable[[T, T], bool] = _default_cmp) -> None:
    """Stable O(n log n) with O(n) extra space.
    Invariant: subarrays [lo, mid) and [mid, hi) sorted before merge.
    """
    tmp: List[T] = [None] * len(a)  # type: ignore

    def merge(lo: int, mid: int, hi: int) -> None:
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            if cmp(a[i], a[j]):
                tmp[k] = a[i]
                i += 1
            else:
                tmp[k] = a[j]
                j += 1
            k += 1
        while i < mid:
            tmp[k] = a[i]
            i += 1
            k += 1
        while j < hi:
            tmp[k] = a[j]
            j += 1
            k += 1
        a[lo:hi] = tmp[lo:hi]

    def sort(lo: int, hi: int) -> None:
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid, hi)
        merge(lo, mid, hi)

    sort(0, len(a))


def quick_sort(a: MutableSequence[T], *, cmp: Callable[[T, T], bool] = _default_cmp) -> None:
    """Unstable average O(n log n), worst O(n^2). In-place.
    Invariant: elements <= pivot placed before partition index.
    """
    def partition(lo: int, hi: int) -> int:
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if cmp(a[j], pivot):
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def sort(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        p = partition(lo, hi)
        sort(lo, p - 1)
        sort(p + 1, hi)

    if a:
        sort(0, len(a) - 1)
