class Solution:
    
    def check(self, stations, mid, k):
        stats = 0
        
        for i in range(len(stations)-1):
            gap = stations[i+1] - stations[i]
            stats += int(gap/mid)
            
            if stats > k:
                return False
        return stats <= k
        
        
    def minMaxDist(self, stations, k):
        # Code here
        low = 0
        high =int(1e8)
        res = high
        
        while (high-low) > 1e-6:
            mid = (low + high)/2.0
            
            if self.check(stations, mid, k):
                res=mid
                high = mid 
            else:
                low = mid 
        return round(res, 6)
                