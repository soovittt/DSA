# Python DSA Tutorial (Theory‑First Implementations)

A practical, theory‑first guide to Data Structures & Algorithms in Python. Each topic pairs a concise concept write‑up with clean, idiomatic reference implementations. No problem sets—just fundamentals, invariants, trade‑offs, and how to implement them correctly.

## Quick Start
- Requirements: Python ≥ 3.10
- Run in place (no install):
  - macOS/Linux
    - `export PYTHONPATH=src`
    - `python -q`
  - Windows (PowerShell)
    - `$env:PYTHONPATH = "src"`
    - `python`
- Try it:
  - `from dsa.lists.singly_linked_list import SinglyLinkedList`
  - `lst = SinglyLinkedList([1,2,3]); list(lst)`

Tip: Read the matching guide under `docs/` before diving into an implementation to internalize invariants and complexity.

## Repository Map
- Docs and guides
  - Foundations: `docs/overview/foundations.md`
  - Structures: `docs/structures/` (lists, hash table, heap, union‑find, deque, LRU/LFU, skip list)
  - Trees: `docs/trees/` (BST, AVL, Red‑Black, B‑Tree, segment/Fenwick, advanced)
  - Graphs/Algos: `docs/algorithms/` (traversals, topo, MST), `docs/graphs/`, `docs/strings/`, `docs/geometry/`, `docs/probabilistic/`
- Reference implementations (importable): `src/dsa/`
  - Lists/Queues/Stacks: `lists/`, `stacks_queues/`
  - Hashing/Caches: `hashing/` (hash table, LRU, LFU)
  - Heaps: `heaps/`
  - Trees: `trees/` (BST, AVL, Red‑Black, B‑Tree, Trie, Segment/Fenwick, Treap, Splay, Order‑Statistics)
  - Graphs: `graphs/` (Graph + BFS/DFS/topo, Dijkstra, Bellman‑Ford, Floyd‑Warshall, MST, Flows)
  - Strings: `strings/` (KMP, Z, Suffix Array + LCP)
  - Algorithms: `searching_sorting/` (search, insertion/merge/quick sort)
  - Patterns: `patterns/patterns.md`

## Learn by Topic (Start Here)
- Concepts: `docs/overview/foundations.md`
- Data Structures
  - Lists: `docs/structures/lists.md` → `src/dsa/lists/singly_linked_list.py`, `src/dsa/lists/doubly_linked_list.py`
  - Stacks/Queues/Deque: `src/dsa/stacks_queues/stack.py`, `queue.py`, `deque_buffer.py`
  - Hash Table: `docs/structures/hash_table.md` → `src/dsa/hashing/hash_table.py`
  - Heaps: `docs/structures/heap.md` → `src/dsa/heaps/binary_heap.py`
  - Union‑Find: `docs/structures/union_find.md` → `src/dsa/union_find/union_find.py`
  - Caches: `docs/structures/lru_cache.md` → `src/dsa/hashing/lru_cache.py`; `docs/structures/lfu.md` → `src/dsa/hashing/lfu_cache.py`
  - Skip List: `docs/structures/skip_list.md` → `src/dsa/lists/skip_list.py`
- Trees
  - BST: `docs/trees/bst.md` → `src/dsa/trees/bst.py`
  - AVL: `docs/trees/avl.md` → `src/dsa/trees/avl.py`
  - Red‑Black: `docs/trees/red_black_tree.md` → `src/dsa/trees/red_black_tree.py`
  - B‑Tree: `docs/trees/btree.md` → `src/dsa/trees/btree.py`
  - Segment/Fenwick: `docs/trees/range_trees.md` → `src/dsa/trees/segment_tree.py`, `src/dsa/trees/fenwick_tree.py`
  - Advanced: `docs/trees/advanced_trees.md` → Treap, Splay, Order‑Statistics
- Graphs & Algorithms
  - Traversals/Topo: `docs/algorithms/graphs.md` → `src/dsa/graphs/graph.py`
  - Shortest Paths: Dijkstra `src/dsa/graphs/dijkstra.py`; Bellman‑Ford/Floyd‑Warshall `src/dsa/graphs/shortest_paths.py`
  - MST: `docs/algorithms/mst.md` → `src/dsa/graphs/mst.py`
  - Flows: `docs/graphs/flows.md` → `src/dsa/graphs/flows.py`
- Strings
  - KMP/Z/SA+LCP: `docs/strings/overview.md` → `src/dsa/strings/`
- Geometry & Probabilistic
  - Convex Hull: `docs/geometry/convex_hull.md` → `src/dsa/geometry/convex_hull.py`
  - Bloom Filter: `docs/probabilistic/bloom_filter.md` → `src/dsa/probabilistic/bloom_filter.py`

## Study Path (Suggested Order)
1) Foundations → Lists/Stacks/Queues → Hash Table → Heap → Union‑Find
2) Trees (BST → AVL → Red‑Black), then Segment/Fenwick
3) Graphs (BFS/DFS → Topo) → Shortest Paths → MST → Flows
4) Strings (KMP/Z → Suffix Array/LCP)
5) Patterns (two pointers, sliding window, monotonic stack/queue, prefix sums, DP)
6) Advanced (B‑Tree, Treap, Splay, Order‑Statistics), Geometry, Probabilistic

## Contributing
- Keep implementations small, readable, and invariant‑driven.
- Prefer clarity over micro‑optimizations.
- Add/update a matching guide in `docs/` when introducing a new structure/algorithm.

Everything is implemented in pure Python with comprehensive docstrings and a focus on correctness and clarity.
