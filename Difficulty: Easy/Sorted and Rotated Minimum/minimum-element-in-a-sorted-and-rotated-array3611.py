"""
# [Sorted and Rotated Minimum](https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return arr[low]

if __name__ == "__main__":
    # Add your test cases here
    pass
