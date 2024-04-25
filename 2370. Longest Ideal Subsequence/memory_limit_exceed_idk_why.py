class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        memo = {}
        def helper(idx, c):
            if (idx, c) in memo:
                return memo[(idx, c)]

            if idx == len(s):
                memo[(idx, c)] = 0
                return 0
            
            # skip
            skip = helper(idx+1, c)
            # keep
            keep = 0
            if abs(ord(s[idx]) - ord(c)) <= k:
                keep = 1 + helper(idx+1, s[idx])
            
            memo[(idx, c)] = max(skip, keep)
            return memo[(idx, c)]
        
        res = 0
        for i,c in enumerate(s):
            helper(i,c)
        
        res = max(memo.values())
        
        return res
