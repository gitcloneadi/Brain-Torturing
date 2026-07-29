"""
# [Kadane's Algorithm](https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def maxSubArraySum(self, arr):
        max_so_far = arr[0]
        curr_max = arr[0]
        for x in arr[1:]:
            curr_max = max(x, curr_max + x)
            max_so_far = max(max_so_far, curr_max)
        return max_so_far

if __name__ == "__main__":
    # Add your test cases here
    pass
