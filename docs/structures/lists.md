# Singly Linked List (Theory & Implementation Notes)

- ADT: sequence with O(1) push_front and O(1) push_back (with tail).
- Invariants: empty => head=tail=None; non-empty => tail.next=None; size tracks nodes.
- Trade-offs: O(1) insert/delete at ends; O(n) search; cache-unfriendly.
- Pitfalls: losing references on delete, incorrect tail maintenance.
- Correctness: maintain invariants on each operation; test via iteration.
