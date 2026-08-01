class Solution:
    
    def check(self, arr, days, k, m):
        boq=0
        cnt=0
        
        
        for flowers in arr:
            if flowers <= days:
               cnt += 1
            else:
                
                boq += cnt//k
                cnt=0
        boq += cnt//k
        return boq >= m
    
    def minDaysBloom(self, arr, k, m):
        # Code here
        low=0
        high=max(arr)
        res=-1
        
        while low <= high:
            mid = low  + (high - low)//2
            
            if self.check(arr, mid, k, m):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
                