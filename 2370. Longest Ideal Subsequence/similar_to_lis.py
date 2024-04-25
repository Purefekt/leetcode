"""
Space optimized dp.

O(n*l) time where l is the number of unique chars, in this case 26.
O(l) space or O(1) in this case since l==26.
"""

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0] * 26

        res = 0
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - cur) <= k:
                    best = max(best, dp[prev])
            
            # append s[i] to the prev longest ideal subsequence
            dp[cur] = max(dp[cur], best+1)
            res = max(res, dp[cur])
        
        return res
