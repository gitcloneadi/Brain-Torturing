"""
# [Bubble Sort](https://www.geeksforgeeks.org/problems/bubble-sort/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

if __name__ == "__main__":
    # Add your test cases here
    pass
