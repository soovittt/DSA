# Trie (Prefix Tree)

- Nodes store map of children; is_word marks completed words.
- Operations: insert, search, starts_with, delete (prune nodes when unused).
- Invariants: root is empty; path corresponds to prefix characters.
