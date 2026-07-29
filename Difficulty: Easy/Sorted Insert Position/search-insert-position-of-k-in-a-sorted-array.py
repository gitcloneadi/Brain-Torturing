"""
# [Sorted Insert Position](https://www.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def searchInsertK(self, arr, k):
        low, high = 0, len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

if __name__ == "__main__":
    # Add your test cases here
    pass
