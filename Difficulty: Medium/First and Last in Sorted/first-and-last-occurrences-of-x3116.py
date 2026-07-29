"""
# [First and Last in Sorted](https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def find(self, arr, x):
        def find_first():
            l, r, res = 0, len(arr) - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == x:
                    res = mid
                    r = mid - 1
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        def find_last():
            l, r, res = 0, len(arr) - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == x:
                    res = mid
                    l = mid + 1
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        return [find_first(), find_last()]

if __name__ == "__main__":
    # Add your test cases here
    pass
