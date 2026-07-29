"""
# [Second Largest](https://www.geeksforgeeks.org/problems/second-largest3735/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def getSecondLargest(self, arr):
        largest = second = -1
        for x in arr:
            if x > largest:
                second = largest
                largest = x
            elif x < largest and x > second:
                second = x
        return second

if __name__ == "__main__":
    # Add your test cases here
    pass
