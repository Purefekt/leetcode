class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        # get all positives
        pos = set()
        for n in nums:
            if n>0:
                pos.add(n)
        
        # get corresponding and track res
        res = -1
        for n in nums:
            if n < 0 and abs(n) in pos:
                res = max(res, abs(n))
        
        return res
