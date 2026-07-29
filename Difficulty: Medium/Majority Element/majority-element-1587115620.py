"""
# [Majority Element](https://www.geeksforgeeks.org/problems/majority-element-1587115620/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def majorityElement(self, arr):
        cand, count = None, 0
        for x in arr:
            if count == 0:
                cand, count = x, 1
            elif x == cand:
                count += 1
            else:
                count -= 1
        if arr.count(cand) > len(arr) // 2:
            return cand
        return -1

if __name__ == "__main__":
    # Add your test cases here
    pass
