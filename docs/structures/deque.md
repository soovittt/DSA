# Deque (Circular Buffer)

- Circular buffer with head/tail indices; one empty slot to distinguish full/empty.
- Resizing doubles capacity; re-enqueue elements preserving order.
- Invariants: indices masked by capacity-1; size tracked separately.
