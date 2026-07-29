"""
# [Anagram](https://www.geeksforgeeks.org/problems/anagram-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
        return Counter(s1) == Counter(s2)

if __name__ == "__main__":
    # Add your test cases here
    pass
