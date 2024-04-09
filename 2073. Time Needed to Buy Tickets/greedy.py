"""
Greedy.
For all people before k and including k, we will add 1 for each round they are a part of.
There will be at max tickets[k] rounds. But if a person has bought all the tickets they can buy, then we wont add.

O(n) time to iterate over the tickets arr in 2 parts.
O(1) space
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        res = 0
        # add the contribution of people upto and including k
        for i in range(k+1):
            res += min(tickets[i], tickets[k])
        
        # for the people AFTER k, their contribution will be tickets[k-1] or their capacity
        for i in range(k+1, len(tickets)):
            res += min(tickets[i], tickets[k]-1)
        
        return res
