import heapq
class Solution:
    def findKClosest(self, arr, k, x):
        # code here
        res = []
        min_heap = []
        
        for num in arr:
            if num != x:
                heapq.heappush(min_heap, (-abs(num-x), num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
            
        return res[::-1]
        
