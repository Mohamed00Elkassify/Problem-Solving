# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Kadane's Algorithm
# Time: O(n)
# Space: O(1)
def maxProfit(prices):
    maxP = 0
    minBuy = prices[0]
    for i in range(1, len(prices)):
        maxP = max(maxP, prices[i] - minBuy)
        minBuy = min(minBuy, prices[i])
    return maxP

# Two Pointers
# Time: O(n)
# Space: O(1)
def maxProfit(prices):
    maxP = 0
    L, R = 0, 1
    while R < len(prices):
        if prices[L] < prices[R]:
            currP = prices[R] - prices[L]
            maxP = max(maxP, currP)
        else:
            L = R
        R += 1
    return maxP