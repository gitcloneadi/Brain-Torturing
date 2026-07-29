"""
# [Sort 0s, 1s and 2s](https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

if __name__ == "__main__":
    # Add your test cases here
    pass
