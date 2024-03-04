"""
Greedy, sort and two pointer.
Always play the lowest token face up and the highest token face down.
First try to play face up to gain score.
If we cant then we must place face down, but only when atleast one token is remaining and score is atleast 1.

O(nlogn) time to sort tokens, then linear time for 2 pointers.
O(n) space used by sorting.
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()

        l = 0
        r = len(tokens)-1

        score = 0
        res = 0
        while l<=r:
            # always play face up when we have enough power
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            
            # if we dont have enough power and atleast one token is remaining, if we have atleast 1 score, play face down
            elif l < r and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            
            # we dont have enough score, power or tokens to place anything to increase score
            else:
                return score
        
        return score
