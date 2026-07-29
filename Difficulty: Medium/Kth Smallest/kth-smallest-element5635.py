"""
# [Kth Smallest](https://www.geeksforgeeks.org/problems/kth-smallest-element5635/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def kthSmallest(self, arr, k):
        return sorted(arr)[k - 1]

if __name__ == "__main__":
    # Add your test cases here
    pass
