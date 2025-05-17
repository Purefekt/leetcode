class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp = [0] * (amount+1)
        for c in coins:
            if c <= amount:
                dp[c] = 1
            
        for i in range(1, len(dp)):
            if dp[i] == 0:
                min_prev = math.inf
                for c in coins:
                    if c<i:
                        min_prev = min(min_prev, dp[i-c])
                    else:
                        break
                dp[i] = min_prev + 1
        
        if dp[-1] == math.inf:
            return -1
        return dp[-1]
        