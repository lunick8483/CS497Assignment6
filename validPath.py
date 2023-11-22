from collections import deque
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph
        graph = [[] for i in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        # BFS traversal
        queue, visited = deque(), set()
        queue.append(source)
        visited.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

solution = Solution()
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(solution.validPath(n,edges,source,destination))
n = 6
edges = [[0,1],[0,2],[3,5],[5,4]]
source = 0
destination = 5
print(solution.validPath(n,edges,source,destination))
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 1
destination = 1
print(solution.validPath(n,edges,source,destination))
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
source = 0
destination = 4
print(solution.validPath(n,edges,source,destination))



