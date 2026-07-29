"""
# [Reverse Words](https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def reverseWords(self, s):
        sep = '.' if '.' in s else ' '
        words = [w for w in s.split(sep) if w]
        return sep.join(words[::-1])

if __name__ == "__main__":
    # Add your test cases here
    pass
