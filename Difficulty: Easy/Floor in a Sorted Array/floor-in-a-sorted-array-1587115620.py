"""
# [Floor in a Sorted Array](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def findFloor(self, arr, k):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

if __name__ == "__main__":
    # Add your test cases here
    pass
