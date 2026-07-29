"""
# [Find Kth Rotation](https://www.geeksforgeeks.org/problems/rotation4723/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == "__main__":
    # Add your test cases here
    pass
