# CS497Assignment6

# Find if Path Exists in Graph
First I'll transform the given edge list into an adjacency list representation of the graph. Each vertex has a list of neighbors, and the size of the list is equal to the number of vertices in the graph. Then I'll set up a queue and  a set to perform a BFS algorithm. I created a queue to perform the breadth-first traversal. Nodes are enqueued and dequeued in the order they are discovered  and visited set to  keeps track of the nodes that have been visited to avoid processing the same node multiple times. The algorithm enters a loop that continues until the queue is empty. Inside the loop, it dequeues a node (node) from the front of the queue. If node is the destination vertex, the function immediately returns True because a valid path has been found. Otherwise, the algorithm iterates through the neighbors of the current node. If a neighbor has not been visited, it is marked as visited and added to the queue. If the BFS traversal completes without encountering the destination vertex, the function returns False. This indicates that there is no valid path from the source to the destination in the graph. <br />
Time complexity is O(V + E), where V is the number of vertices and E is the number of edges.<br />
Space complexity is is O(V + E), where V is the number of vertices and E is the number of edges.<br />

# Longest Cycle in a Graph
I'll try to find Strongly Connected Components (SCCs) in a directed graph. SCCs are subsets of nodes in a graph where each node is reachable from every other node within the subset. I'll uses DFS to identify SCCs in the directed graph. First I'll Perform a DFS on the reversed graph to obtain a reverse topological order of the nodes. Then I'll perform another DFS on the original graph, considering nodes in the reverse topological order obtained in the first step. During this DFS, I also keep track of the SCC with the maximum number of nodes (the one that forms the longest cycle). <br />
Time Complexity: O(n)  <br />
Space Complexity: O(n)  <br />

# Connecting Cities with minimum Cost

# All Paths From Source to Target
