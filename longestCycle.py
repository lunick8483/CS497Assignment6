class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        N = len(edges)

        # Constructing the reversed graph
        reverse_graph = [[] for _ in range(N)]
        for u, v in enumerate(edges):
            if v != -1:
                reverse_graph[v].append(u)

        # First DFS to obtain reverse topological order
        back_order = []
        visited = [False for _ in range(N)]

        def dfs(u):
            visited[u] = True
            v = edges[u]
            if not visited[v] and v != -1:
                dfs(v)
            back_order.append(u)

        for i in range(N):
            if not visited[i]:
                dfs(i)

        back_order.reverse()

        # Second DFS to find the size of each SCC and update the maximum count
        visited = [False for _ in range(N)]
        global cnt
        cnt = 0

        def reverse_dfs(u):
            global cnt
            visited[u] = True
            cnt += 1
            for v in reverse_graph[u]:
                if not visited[v]:
                    reverse_dfs(v)

        ans = 1
        for u in back_order:
            if not visited[u]:
                cnt = 0
                reverse_dfs(u)
                ans = max(ans, cnt)

        return -1 if ans == 1 else ans

solution = Solution()
edges = [3,3,4,2,3]
print(solution.longestCycle(edges))
edges = [2,-1,3,1]
print(solution.longestCycle(edges))

