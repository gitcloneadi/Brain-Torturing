class Solution:
    
    def check(self, arr, mid, k):
        total=0
        for i in range(len(arr)):
            total += (arr[i] + mid - 1) // mid
        return total <= k
        
    
    def kokoEat(self, arr, k):
        # Code here
        low = 1
        high = max(arr)
        res = high
        while low <= high:
            mid = low + (high-low)//2
            if self.check(arr, mid, k):
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        return res
