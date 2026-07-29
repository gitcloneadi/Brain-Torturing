"""
# [Alternate Positive Negative](https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def rearrange(self, arr):
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        i = j = k = 0
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1
            arr[k] = neg[j]
            k += 1
            j += 1
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1

if __name__ == "__main__":
    # Add your test cases here
    pass
