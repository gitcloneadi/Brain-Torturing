"""
# [Level order traversal](https://www.geeksforgeeks.org/problems/level-order-traversal/0)
# Difficulty Level : Difficulty: Medium
"""

from collections import deque
class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            node = q.popleft()
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

if __name__ == "__main__":
    # Add your test cases here
    pass
