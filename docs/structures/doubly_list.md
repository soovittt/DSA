# Doubly Linked List

- Sentinels simplify edge cases (no null checks on ends).
- O(1) insert/remove with node reference; O(n) search.
- Invariants: head.prev=None, tail.next=None; empty => head.next=tail, tail.prev=head.
