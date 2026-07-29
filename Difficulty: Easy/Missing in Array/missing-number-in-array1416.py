"""
# [Missing in Array](https://www.geeksforgeeks.org/problems/missing-number-in-array1416/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        return n * (n + 1) // 2 - sum(arr)

if __name__ == "__main__":
    # Add your test cases here
    pass
