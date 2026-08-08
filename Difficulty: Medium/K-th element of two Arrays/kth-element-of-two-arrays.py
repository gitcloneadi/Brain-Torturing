class Solution:
    def kthElement(self, a, b, k):
        # code here
        n=len(a)
        m=len(b)
        sorted=[]
        
        i=0
        j=0
        while i < n and j < m:
            if a[i]<b[j]:
                sorted.append(a[i])
                i+=1
            else:
                sorted.append(b[j])
                j+=1
        while i < n:
            sorted.append(a[i])
            i+=1
        while j < m:
            sorted.append(b[j])
            j+=1
        
        return sorted[k-1]