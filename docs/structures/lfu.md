# LFU Cache

- Frequency buckets map freq -> ordered keys; min_freq tracks eviction bucket.
- get: return value and bump key's frequency.
- put: evict LRU from min_freq when at capacity; insert with freq=1.
