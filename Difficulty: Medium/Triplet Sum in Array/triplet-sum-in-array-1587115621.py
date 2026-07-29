"""
# [Triplet Sum in Array](https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def find3Numbers(self, arr, target):
        arr.sort()
        n = len(arr)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return False

if __name__ == "__main__":
    # Add your test cases here
    pass
