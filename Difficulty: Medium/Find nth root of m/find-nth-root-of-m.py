import math

class Solution:
    def nthRoot(self, n, m):
       # code here
        if n==0 or m==0:
           return 0
        po=1/n
       
        res = int(math.exp(po*math.log(m)))
        
        
        if (res)**n==m:
            return res
        if (res+1)**n==m:
           return res + 1
        else:
            return -1
        
         
        
