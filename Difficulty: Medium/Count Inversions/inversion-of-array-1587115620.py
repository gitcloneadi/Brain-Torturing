"""
# [Count Inversions](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += merge_sort(arr, left, mid)
                inv_count += merge_sort(arr, mid + 1, right)
                inv_count += merge(arr, left, mid, right)
            return inv_count

        def merge(arr, left, mid, right):
            i, j = left, mid + 1
            temp = []
            inv_count = 0
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv_count += (mid - i + 1)
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            for k in range(len(temp)):
                arr[left + k] = temp[k]
            return inv_count

        return merge_sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    # Add your test cases here
    pass
