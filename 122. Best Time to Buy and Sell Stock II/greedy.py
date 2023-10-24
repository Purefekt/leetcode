"""
Since we know the future, thus we know when the stock goes down and up.
So we need to buy and sell the stock every single time when the stock goes from a lower value to a higher value.
Check from 0th index till 2nd last index, since to sell a stock, we need to be able to buy it first.
Buy only when the next stock is higher and then sell and add to profit.

O(n) time to iterate through the prices list once.
O(1) space.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for i in range(len(prices)-1):
            # Assume we bought at i-1, so we need to sell when i is > i-1
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        
        return profit
