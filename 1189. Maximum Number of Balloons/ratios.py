class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        req = {
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }

        freq = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }

        for c in text:
            if c in freq:
                freq[c] += 1
        
        # get ratios
        min_rat = math.inf
        for c in freq:
            cur_rat = freq[c] // req[c]
            min_rat = min(min_rat, cur_rat)
        
        return min_rat
        