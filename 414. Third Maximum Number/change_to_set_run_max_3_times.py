class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # convert array to set to get unique values
        nums = set(nums)
        
        if len(nums) < 3:
            return max(nums)
        
        # remove the 3 max elements and return the last
        maxx = max(nums)
        nums.remove(maxx)
        
        maxx = max(nums)
        nums.remove(maxx)
        
        return max(nums)
    