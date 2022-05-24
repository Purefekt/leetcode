class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        # i is buy, j is sell
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                # sell must be larger than buy
                if prices[j] > prices[i]:
                    # sell must be atleast larger than current max profit
                    if max_profit < prices[j]:
                        profit = prices[j] - prices[i]
                        max_profit = max(max_profit, profit)
                
            
        return max_profit

    
# exceeding time limit