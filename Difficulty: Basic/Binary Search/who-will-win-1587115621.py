"""
# [Binary Search](https://www.geeksforgeeks.org/problems/who-will-win-1587115621/0)
# Difficulty Level : Difficulty: Basic
"""

class Solution:
    def binarysearch(self, arr, k):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == "__main__":
    # Add your test cases here
    pass
