"""
# [Equilibrium Point](https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        for i, val in enumerate(arr):
            if left_sum == total_sum - left_sum - val:
                return i
            left_sum += val
        return -1

if __name__ == "__main__":
    # Add your test cases here
    pass
