"""
# [Duplicates in a Limited Range Array](https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def duplicates(self, arr):
        seen = set()
        dups = set()
        for x in arr:
            if x in seen:
                dups.add(x)
            seen.add(x)
        return sorted(list(dups)) if dups else [-1]

if __name__ == "__main__":
    # Add your test cases here
    pass
