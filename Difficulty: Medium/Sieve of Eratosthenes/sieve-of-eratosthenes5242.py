"""
# [Sieve of Eratosthenes](https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def sieveOfEratosthenes(self, n):
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

if __name__ == "__main__":
    # Add your test cases here
    pass
