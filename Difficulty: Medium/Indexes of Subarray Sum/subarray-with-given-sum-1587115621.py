"""
# [Indexes of Subarray Sum](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        left = 0
        curr_sum = 0
        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target and left < right:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == target:
                return [left + 1, right + 1]
        return [-1]

if __name__ == "__main__":
    # Add your test cases here
    pass
