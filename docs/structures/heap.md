# Binary Heap (Min/Max)

- Invariants: parent <= children (min-heap) or >= (max-heap); complete tree shape.
- Array layout: children of i are 2i+1, 2i+2; parent is floor((i-1)/2).
- Operations: push (sift-up), pop (sift-down), peek; heapify in O(n).
- Pitfalls: wrong comparisons; forgetting shape constraint during swaps.
