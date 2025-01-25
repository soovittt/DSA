class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        in_degree = [0]*numCourses
        for (course, prereq) in prerequisites:
            if prereq in graph.keys():
                graph[prereq]  = course
            else:
                graph[prereq] = [course]
            in_degree[course] += 1
        q = [i for i in range(numCourses) if in_degree[i] == 0]
        topo_order = []
        while q:
            node = q.pop()
            topo_order.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1  # Remove dependency
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        if len(topo_order) == numCourses:return topo_order  # Valid topological order
        else:return []  # Cycle detected, return empty list



sol = Solution()
print(sol.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))