"""
# [Min Add to Make Parentheses Valid](https://www.geeksforgeeks.org/problems/min-add-to-make-parentheses-valid/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def minParentheses(self, s):
        open_cnt = close_cnt = 0
        for ch in s:
            if ch == '(':
                open_cnt += 1
            elif open_cnt > 0:
                open_cnt -= 1
            else:
                close_cnt += 1
        return open_cnt + close_cnt

if __name__ == "__main__":
    # Add your test cases here
    pass
