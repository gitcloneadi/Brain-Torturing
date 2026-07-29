"""
# [First Occurrence in Sorted](https://www.geeksforgeeks.org/problems/binary-search-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def firstOccurrence(self, arr, target):
        low, high = 0, len(arr) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                res = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

if __name__ == "__main__":
    # Add your test cases here
    pass
