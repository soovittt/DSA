class Solution:
    def build_adj_list(self,n,edges):
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    def validPath(self, n, edges, source, destination):
        adj_list = self.build_adj_list(n,edges)
        visited = set()
        q = [source]
        while q:
            node = q.pop()
            if node == destination:
                return True 
            if node not in visited:
                visited.add(node)
                for neighbour in adj_list[node]:
                    if neighbour not in visited:
                        q.append(neighbour)
        return False




sol = Solution()
print(sol.validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5))