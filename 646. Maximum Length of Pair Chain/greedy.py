"""
Greedy.
Sort by the end of the pair.
Intuition: If we have 2 intervals which start at the same time, then if we pick the one which ends first, this one will always form a chain with every single pair which forms a chain with the one which ends later.
Use ends to determine when to take a new interval, everytime we take a new one, increment count.

O(nlogn) time to sort.
O(n) space used by sorting. Otherwise constant space.
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # sort by end timings
        pairs.sort(key = lambda x: x[1])

        res = 1
        start = pairs[0][0]
        end = pairs[0][1]

        for i in range(1,len(pairs)):
            s_i =  pairs[i][0]
            e_i = pairs[i][1]

            if s_i > end:
                res += 1
                start = s_i
                end = e_i
        
        return res
