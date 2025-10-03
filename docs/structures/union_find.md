# Union-Find (Disjoint Set Union)

- Invariants: forest of trees; parent[x] is representative; rank guides union.
- Optimizations: union by rank/size; path compression.
- Complexity: almost O(1) amortized (inverse Ackermann).
- Use cases: connectivity, Kruskal's MST, dynamic connectivity.
