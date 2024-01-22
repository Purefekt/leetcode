class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        freq = {i:0 for i in range(1, n+1)}

        for n in nums:
            freq[n] += 1
        
        twice = None
        missed = None
        for k,v in freq.items():
            if v == 2:
                twice = k
            elif v == 0:
                missed = k
        
        return [twice, missed]
        