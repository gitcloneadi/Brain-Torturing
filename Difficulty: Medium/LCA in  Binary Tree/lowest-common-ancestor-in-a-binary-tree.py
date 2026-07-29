"""
# [LCA in  Binary Tree](https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def lca(self, root, n1, n2):
        if not root or root.data == n1 or root.data == n2:
            return root
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        if left and right:
            return root
        return left if left else right

if __name__ == "__main__":
    # Add your test cases here
    pass
