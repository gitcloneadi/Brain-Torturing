"""
# [Reverse a Linked List](https://www.geeksforgeeks.org/problems/reverse-a-linked-list/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

if __name__ == "__main__":
    # Add your test cases here
    pass
