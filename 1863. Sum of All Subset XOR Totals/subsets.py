class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(idx, total):
            if idx == len(nums):
                return total
            
            keep = backtrack(idx+1, total^nums[idx])
            skip = backtrack(idx+1, total)
            return keep + skip
        
        return backtrack(0, 0)
