# represent the course in graph . each prereq array is a graph edge 
# then detect cycles

class Solution:

    def has_cycle(self, graph):
        visited = set()
        recursion_stack = set()

        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                elif neighbour in recursion_stack:
                    return True
            recursion_stack.remove(node)
            return False

        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False  # Added this return statement to complete the function

    def canFinish(self, numCourses, prerequisites):
        graph = {}
        
        # Build the adjacency list
        for course, prereq in prerequisites:
            if prereq in graph:
                graph[prereq].append(course)
            else:
                graph[prereq] = [course]

        # Check for cycles in the graph
        if self.has_cycle(graph):
            return False

        return True


sol = Solution()
print(sol.canFinish(2,[[1,0]]))