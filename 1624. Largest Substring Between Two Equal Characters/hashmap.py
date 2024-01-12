class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        occurance = {}
        for i,c in enumerate(s):
            if c not in occurance:
                occurance[c] = [i,i]
            else:
                occurance[c][1] = i
        
        res = 0
        for v in occurance.values():
            res = max(res, v[1]-v[0])
        
        return res-1
        