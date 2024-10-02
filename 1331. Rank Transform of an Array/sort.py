"""
Sort with indexes and rebuild the result with rank.

O(nlogn) time.
O(n) space.
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        res = [0] * len(arr)
        arr = [(n,i) for i,n in enumerate(arr)]

        arr.sort()
        rank = 0
        cur = -math.inf
        for num, idx in arr:
            if num != cur:
                rank += 1
                cur = num
            res[idx] = rank
        
        return res
