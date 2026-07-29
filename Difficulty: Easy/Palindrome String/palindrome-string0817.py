"""
# [Palindrome String](https://www.geeksforgeeks.org/problems/palindrome-string0817/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, s):
        return 1 if s == s[::-1] else 0

if __name__ == "__main__":
    # Add your test cases here
    pass
