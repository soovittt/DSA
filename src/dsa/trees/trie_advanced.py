from __future__ import annotations
from typing import List, Optional

from .trie import Trie, TrieNode


class TrieAdvanced(Trie):
    """Extends Trie with wildcard search and autocomplete.

    Wildcard: '.' matches any single character.
    Autocomplete: collects words with given prefix, optional limit k.
    """

    def wildcard_search(self, pattern: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(pattern):
                return node.is_word
            ch = pattern[i]
            if ch == '.':
                for nxt in node.children.values():
                    if dfs(nxt, i + 1):
                        return True
                return False
            nxt = node.children.get(ch)
            return False if nxt is None else dfs(nxt, i + 1)
        return dfs(self.root, 0)

    def autocomplete(self, prefix: str, k: Optional[int] = None) -> List[str]:
        # find node for prefix
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return []
        out: List[str] = []

        def collect(n: TrieNode, path: List[str]) -> None:
            if k is not None and len(out) >= k:
                return
            if n.is_word:
                out.append(prefix + ''.join(path))
                if k is not None and len(out) >= k:
                    return
            for ch, nxt in n.children.items():
                path.append(ch)
                collect(nxt, path)
                path.pop()

        collect(node, [])
        return out
