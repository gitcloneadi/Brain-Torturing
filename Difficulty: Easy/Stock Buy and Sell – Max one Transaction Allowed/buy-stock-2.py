"""
# [Stock Buy and Sell – Max one Transaction Allowed](https://www.geeksforgeeks.org/problems/buy-stock-2/0)
# Difficulty Level : Difficulty: Easy
"""

class Solution:
    def maximumProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit

if __name__ == "__main__":
    # Add your test cases here
    pass
