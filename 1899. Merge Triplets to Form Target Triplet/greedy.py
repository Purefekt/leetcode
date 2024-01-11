"""
For all 3 places, we want arrays where that space == that index in target and the other 2 indexes are <= other 2 in target.
Set first flag to false and go through all triplets.
If we find an array where triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2], then we can get First.
If we go through all the triplets and do not get a valid array, return False
Repeat this for other 2 as well.
If all three are true, return True.

O(n) time since we do 3 passes over triplets.
O(1) space since we use flags.
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # find first valid
        first = False
        for f,s,t in triplets:
            if f == target[0]:
                if s <= target[1] and t <= target[2]:
                    first = True
                    break
        
        if first is False: return False

        # find second valid
        second = False
        for f,s,t in triplets:
            if s == target[1]:
                if f <= target[0] and t <= target[2]:
                    second = True
                    break
        
        if second is False: return False

        # find third valid
        third = False
        for f,s,t in triplets:
            if t == target[2]:
                if f <= target[0] and s <= target[1]:
                    third = True
                    break
        
        if third is False: return False

        return True
        