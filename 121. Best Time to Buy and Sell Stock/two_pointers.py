class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 0 # sell
        max_profit = 0

        # stop when right pointer or sell has reached the end of array
        while(r<len(prices)):
            # if sell(r) is more than buy(l)
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                # track max profit
                max_profit = max(profit, max_profit)
                
                # move right pointer
                r = r + 1
            # else if sell is less than buy, just set the left pointer to right pointer and move right pointer
            else:
                l = r
                r = r + 1
        
        return max_profit
                