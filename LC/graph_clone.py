from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = set()
        q = [node]
        mapping = {}
        mapping[node] =  Node(node.val)
        while q:
            current = q.pop()
            for neighbour in current.neighbors:
                if neighbour not in mapping:
                    mapping[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                mapping[current].neighbors.append(mapping[neighbour])
        return mapping[node]




sol = Solution()