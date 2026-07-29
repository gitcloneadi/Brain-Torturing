"""
# [Dijkstra Algorithm](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/0)
# Difficulty Level : Difficulty: Medium
"""

import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        dist = [float('inf')] * V
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

if __name__ == "__main__":
    # Add your test cases here
    pass
