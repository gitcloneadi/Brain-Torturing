"""
# [Missing And Repeating](https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        S = sum(arr)
        S_sq = sum(x * x for x in arr)
        expected_S = n * (n + 1) // 2
        expected_S_sq = n * (n + 1) * (2 * n + 1) // 6
        diff = S - expected_S  # x - y
        sum_xy = (S_sq - expected_S_sq) // diff  # x + y
        x = (diff + sum_xy) // 2
        y = sum_xy - x
        return [x, y]

if __name__ == "__main__":
    # Add your test cases here
    pass
