"""
# [Validate an IP Address](https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/0)
# Difficulty Level : Difficulty: Medium
"""

class Solution:
    def isValid(self, str):
        parts = str.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if not p.isdigit() or (len(p) > 1 and p[0] == '0') or not (0 <= int(p) <= 255):
                return False
        return True

if __name__ == "__main__":
    # Add your test cases here
    pass
