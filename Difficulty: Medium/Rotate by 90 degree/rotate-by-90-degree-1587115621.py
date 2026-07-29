"""
# [Rotate by 90 degree](https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def rotateby90(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n // 2):
            mat[i], mat[n - 1 - i] = mat[n - 1 - i], mat[i]

if __name__ == "__main__":
    # Add your test cases here
    pass
