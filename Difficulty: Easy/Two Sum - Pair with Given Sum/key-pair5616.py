"""
# [Two Sum - Pair with Given Sum](https://www.geeksforgeeks.org/problems/key-pair5616/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for num in arr:
            if target - num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    # Add your test cases here
    pass
