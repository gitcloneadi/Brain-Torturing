"""
# [Minimum Spanning Tree](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/0)
# Difficulty Level : Difficulty: Medium
"""

import heapq
class Solution:
    def spanningTree(self, V, adj):
        visited = [False] * V
        min_heap = [(0, 0)]
        res = 0
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            res += weight
            for v, w in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        return res

if __name__ == "__main__":
    # Add your test cases here
    pass
