"""
# [Linked List End Insertion](https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0)
# Difficulty Level : Difficulty: Basic
"""

class Solution:
    def insertAtEnd(self, head, x):
        from gfg import Node # Standard GFG Node representation
        new_node = Node(x)
        if not head:
            return new_node
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head

if __name__ == "__main__":
    # Add your test cases here
    pass
