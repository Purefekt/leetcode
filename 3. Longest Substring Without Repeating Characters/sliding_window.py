class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        
        res = 0
        cur = set()
        for r in range(len(s)):
            if s[r] in cur:
                # shift l till we cross the char which caused repetition
                while s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                l += 1
            else:
                cur.add(s[r])
            res = max(res, r-l+1)
        
        return res
