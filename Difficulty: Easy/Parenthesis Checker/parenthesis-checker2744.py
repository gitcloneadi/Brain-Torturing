"""
# [Parenthesis Checker](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def isBalanced(self, s):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in matching.values():
                stack.append(ch)
            elif ch in matching:
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
        return len(stack) == 0

if __name__ == "__main__":
    # Add your test cases here
    pass
