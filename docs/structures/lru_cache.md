# LRU Cache

- Hash map for O(1) key lookup; doubly linked list for O(1) recency updates.
- Evict from tail when at capacity; move accessed/updated nodes to head.
- Invariants: head.next is MRU; tail.prev is LRU; sentinels present.
