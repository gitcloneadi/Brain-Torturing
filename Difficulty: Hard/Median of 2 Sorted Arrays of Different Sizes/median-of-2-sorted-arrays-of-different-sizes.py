class Solution:
    def medianOf2(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        
        if n > m:
            return self.medianOf2(b, a)
        
        low  = 0
        high = n
        
        while low <= high:
            mid1 = low + (high-low)//2
            mid2 = (n + m +1)//2 - mid1
            
            l1 = (mid1==0 and float('-inf') or a[mid1-1])
            r1 = (mid1==n and float('inf') or a[mid1])
            l2 = (mid2==0 and float('-inf') or b[mid2-1])
            r2 = (mid2==m and float('inf') or b[mid2])
            
            if l1 <= r2 and l2 <= r1:
                if (n+m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0