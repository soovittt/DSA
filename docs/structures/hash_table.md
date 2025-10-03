# Hash Table (Open Addressing with Linear Probing)

- Invariant: load factor <= threshold; probe sequence preserved by tombstones.
- Complexity: expected O(1) set/get/delete under low load; O(n) worst-case.
- Resizing: double capacity (power of two) and reinsert live entries.
- Pitfalls: failing to reuse tombstones; not resizing; poor hash functions.
