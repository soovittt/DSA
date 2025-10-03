# Max Flow

- Edmonds-Karp: BFS-level augmenting paths; O(VE^2).
- Dinic: level graph + blocking flow; O(EV^2) general, faster in practice.
- Invariants: residual capacity and flow conservation at each augmentation.
