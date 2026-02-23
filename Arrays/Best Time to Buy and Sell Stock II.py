# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Greedy
# Time: O(n)
# Space: O(1)
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit