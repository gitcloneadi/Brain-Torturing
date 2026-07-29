class Solution:
    def longestConsecutive(self, arr):
        # code here
        res=1
        cnt=1
        arr.sort()
        
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1]:
                continue
            if arr[i] == (arr[i-1]+1):
                cnt+=1
            else:
                cnt=1
            res=max(res, cnt)
        
        return res