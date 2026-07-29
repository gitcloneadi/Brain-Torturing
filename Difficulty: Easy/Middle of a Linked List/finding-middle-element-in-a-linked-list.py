"""
# [Middle of a Linked List](https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def getMiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else -1

if __name__ == "__main__":
    # Add your test cases here
    pass
