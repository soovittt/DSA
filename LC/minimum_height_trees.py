from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = deque([node for node in graph if len(graph[node]) == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()  
                neighbour = graph[leaf].pop()  
                graph[neighbour].remove(leaf)  
                if len(graph[neighbour]) == 1:
                    leaves.append(neighbour)
        return list(leaves)


sol = Solution()
print(sol.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))