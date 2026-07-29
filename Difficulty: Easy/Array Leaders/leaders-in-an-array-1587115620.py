"""
# [Array Leaders](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def leaders(self, arr):
        n = len(arr)
        max_right = arr[-1]
        res = [max_right]
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_right:
                max_right = arr[i]
                res.append(arr[i])
        return res[::-1]

if __name__ == "__main__":
    # Add your test cases here
    pass
