"""
Dynamic programming
Init the dp hashmap with len(s):1
Run a loop from i-1 to 0
to add 1 char, dp[i] = dp[i+1]
If adding 2 chars is valid, add dp[i+2] to dp[i]
Solution at dp[0]

O(n) time
O(n) space
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                # add 1 char
                dp[i] = dp[i+1]
                
                if i<len(s)-1:
                    if int(s[i:i+2]) <= 26:
                        dp[i] += dp[i+2]
        
        return dp[0]
        