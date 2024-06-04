class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get freq of each
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        
        # keep the max even count possible and update hashmap
        res = 0
        for k,v in freq.items():
            res += (v//2) * 2
            freq[k] -= (v//2) * 2
        
        # if any odd char is left, add 1 to res
        for k,v in freq.items():
            if v == 1:
                res += 1
                break

        return res
