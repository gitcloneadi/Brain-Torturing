class Solution:
    def subarrayXor(self, arr, m):
        # code here
        freq={}
        
        pxor = 0
        count=0
        
        for nums in arr:
            pxor ^= nums
            
            count += freq.get(pxor ^ k, 0)
            
            if pxor == k:
                count+=1
            freq[pxor] = freq.get(pxor, 0) + 1
        
        return count