"""
# [Max Sum Subarray of size K](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def maximumSumSubarray(self, k, arr):
        n = len(arr)
        curr_sum = sum(arr[:k])
        max_sum = curr_sum
        for i in range(k, n):
            curr_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum

if __name__ == "__main__":
    # Add your test cases here
    pass
