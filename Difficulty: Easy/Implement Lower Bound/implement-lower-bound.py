"""
# [Implement Lower Bound](https://www.geeksforgeeks.org/problems/implement-lower-bound/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def lowerBound(self, arr, target):
        low, high = 0, len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

if __name__ == "__main__":
    # Add your test cases here
    pass
