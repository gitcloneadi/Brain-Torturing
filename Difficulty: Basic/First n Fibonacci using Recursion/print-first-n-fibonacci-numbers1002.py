"""
# [First n Fibonacci using Recursion](https://www.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/0)
# Difficulty Level : Difficulty: Basic
"""

class Solution:
    def fibonacciNumbers(self, n):
        res = [0, 1]
        for _ in range(2, n):
            res.append(res[-1] + res[-2])
        return res[:n]

if __name__ == "__main__":
    # Add your test cases here
    pass
