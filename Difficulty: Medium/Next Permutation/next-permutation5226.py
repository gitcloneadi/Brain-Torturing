"""
# [Next Permutation](https://www.geeksforgeeks.org/problems/next-permutation5226/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return arr

if __name__ == "__main__":
    # Add your test cases here
    pass
