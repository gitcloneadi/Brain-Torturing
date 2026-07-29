"""
# [Palindrome Linked List](https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def isPalindrome(self, head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.data)
            curr = curr.next
        return vals == vals[::-1]

if __name__ == "__main__":
    # Add your test cases here
    pass
