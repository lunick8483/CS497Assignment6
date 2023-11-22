class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target_node = len(graph) - 1
        all_paths = []
        current_paths = []

        # Initialize paths with neighbors of the source node (0)
        for i in graph[0]:
            current_paths.append([0, i])

        # Explore paths until none are left
        while current_paths:
            node = current_paths.pop()

            # Check if the last node of the current path is the target node
            if node[-1] == target_node:
                all_paths.append(node)
            else:
                # Explore neighbors and add new paths to the list
                if graph[node[-1]]:
                    for i in graph[node[-1]]:
                        current_paths.append(node + [i])

        return all_paths

solution = Solution()
graph = [[1, 2], [3], [3], []]
print(solution.allPathsSourceTarget(graph))
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(solution.allPathsSourceTarget(graph))



