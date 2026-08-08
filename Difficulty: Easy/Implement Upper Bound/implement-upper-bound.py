class Solution:
    def upperBound(self, arr, target):
        # code here
        i=0
        while i < len(arr):
            if arr[i] > target:
                return i
                break
            i+=1
        return len(arr)
            