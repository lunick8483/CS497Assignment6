class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Sort connections based on cost
        connections.sort(key=lambda x: x[2])

        # Initialize parent array for Union-Find
        parent = list(range(n))

        total_cost = 0
        remaining_nodes = n

        # Kruskal's algorithm
        for x, y, cost in connections:
            x, y = x - 1, y - 1  # Convert to 0-indexing

            # Check if nodes x and y are in different sets
            if find(x) != find(y):
                # Merge the sets
                parent[find(x)] = find(y)
                total_cost += cost
                remaining_nodes -= 1

                # If all nodes are connected, return the total cost
                if remaining_nodes == 1:
                    return total_cost

        # If not all nodes are connected, return -1
        return -1

solution = Solution()
n = 3
connections = [[1,2,5],[1,3,6],[2,3,1]]
print(solution.minimumCost(n,connections))
n = 4
connections = [[1,2,3],[3,4,4]]
print(solution.minimumCost(n,connections))
