# Minimum Spanning Tree (MST)

## Kruskal
- Sort edges; add if it doesn't form a cycle (Union-Find). O(E log E).

## Prim
- Grow tree from a start node using a min-heap frontier. O(E log V).

- Both produce minimal total weight spanning all vertices (if connected).
