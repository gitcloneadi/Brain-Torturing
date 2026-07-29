"""
# [Insertion Sort](https://www.geeksforgeeks.org/problems/insertion-sort/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

if __name__ == "__main__":
    # Add your test cases here
    pass
