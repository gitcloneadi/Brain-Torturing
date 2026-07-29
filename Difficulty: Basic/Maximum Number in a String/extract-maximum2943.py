"""
# [Maximum Number in a String](https://www.geeksforgeeks.org/problems/extract-maximum2943/0)
# Difficulty Level : Difficulty: Basic
"""

import re
class Solution:
    def extractMaximum(self, s):
        nums = [int(x) for x in re.findall(r'\d+', s)]
        return max(nums) if nums else -1

if __name__ == "__main__":
    # Add your test cases here
    pass
