"""
Dp top down with memoization.
At each price, we can either buy, or skip. 
But actually we can either buy or skip OR sell or skip.
So we maintain a boolean flag status, False means we dont have any stock and can buy or skip.
True means we have stock and can sell or skip.
If we buy, we move to the next index, if we sell we move to the next.next index due to cooldown.
Recursive function takes (idx, status). Memoiz on it.

O(n) time since we have number of element * status computations, but there can only be 2 states, thus 2*n.
O(n) space to store the 2*n (idx, status) combos.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # status = False -> Dont have any stock, can only buy or skip
        # status = True -> Have stock, can only sell or skip
        memo = {}
        def helper(idx, status):
            if (idx, status) in memo:
                return memo[(idx, status)]

            if idx >= len(prices):
                memo[(idx, status)] = 0
                return 0
            
            if status is False:
                buy = helper(idx+1, True) - prices[idx]
                skip = helper(idx+1, status)
                memo[(idx, status)] = max(buy, skip)
                return max(buy, skip)
            
            else:
                sell = helper(idx+2, False) + prices[idx]
                skip = helper(idx+1, status)
                memo[(idx, status)] = max(sell, skip)
                return max(sell, skip)
        
        return helper(0, False)
