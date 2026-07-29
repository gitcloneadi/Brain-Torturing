"""
# [Set Matrix Zeros](https://www.geeksforgeeks.org/problems/set-matrix-zeroes/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        first_row_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_zero = any(mat[i][0] == 0 for i in range(n))
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0
        if first_col_zero:
            for i in range(n):
                mat[i][0] = 0

if __name__ == "__main__":
    # Add your test cases here
    pass
