class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            res.append(nums[i])
        for i in range(len(nums)):
            res.append(nums[i])
        
        return res
        