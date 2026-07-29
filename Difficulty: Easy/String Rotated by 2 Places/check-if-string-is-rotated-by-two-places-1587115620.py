"""
# [String Rotated by 2 Places](https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def isRotated(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) <= 2:
            return s1 == s2
        left_rot = s1[2:] + s1[:2]
        right_rot = s1[-2:] + s1[:-2]
        return s2 == left_rot or s2 == right_rot

if __name__ == "__main__":
    # Add your test cases here
    pass
