"""
# [Primes in a Range](https://www.geeksforgeeks.org/problems/find-prime-numbers-in-a-range4718/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def primeRange(self, M, N):
        if N < 2:
            return []
        sieve = [True] * (N + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(N**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, N + 1, i):
                    sieve[j] = False
        return [i for i in range(max(2, M), N + 1) if sieve[i]]

if __name__ == "__main__":
    # Add your test cases here
    pass
