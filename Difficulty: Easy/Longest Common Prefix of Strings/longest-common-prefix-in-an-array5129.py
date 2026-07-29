"""
# [Longest Common Prefix of Strings](https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        arr.sort()
        first, last = arr[0], arr[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        res = first[:i]
        return res if res else "-1"

if __name__ == "__main__":
    # Add your test cases here
    pass
