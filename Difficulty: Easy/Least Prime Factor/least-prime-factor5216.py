"""
# [Least Prime Factor](https://www.geeksforgeeks.org/problems/least-prime-factor5216/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def leastPrimeFactor(self, n):
        res = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if res[i] == i:
                for j in range(i * i, n + 1, i):
                    if res[j] == j:
                        res[j] = i
        return res

if __name__ == "__main__":
    # Add your test cases here
    pass
