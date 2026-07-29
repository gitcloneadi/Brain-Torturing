"""
# [BFS of graph](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/0)
# Difficulty Level : Difficulty: Easy
"""

from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        visited = [False] * V
        res = []
        queue = deque([0])
        visited[0] = True
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return res

if __name__ == "__main__":
    # Add your test cases here
    pass
