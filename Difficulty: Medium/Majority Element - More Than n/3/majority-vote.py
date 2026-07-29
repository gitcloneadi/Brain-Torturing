"""
# [Majority Element - More Than n/3](https://www.geeksforgeeks.org/problems/majority-vote/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for x in arr:
            if cand1 == x:
                count1 += 1
            elif cand2 == x:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = x, 1
            elif count2 == 0:
                cand2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        for cand in [cand1, cand2]:
            if cand is not None and arr.count(cand) > n // 3:
                res.append(cand)
        return sorted(res)

if __name__ == "__main__":
    # Add your test cases here
    pass
