from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_word: bool = False


class Trie:
    """Prefix tree supporting insert/search/starts_with/delete.

    Invariants:
    - Root is empty node; paths represent prefixes; is_word marks terminal.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def delete(self, word: str) -> bool:
        def _del(node: TrieNode, i: int) -> bool:
            if i == len(word):
                if not node.is_word:
                    return False
                node.is_word = False
                return len(node.children) == 0
            ch = word[i]
            child = node.children.get(ch)
            if not child:
                return False
            should_delete = _del(child, i + 1)
            if should_delete:
                del node.children[ch]
            return not node.is_word and len(node.children) == 0
        return _del(self.root, 0)

    def _find_node(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node
