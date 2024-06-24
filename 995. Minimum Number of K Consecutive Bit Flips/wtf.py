class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        flipped = [False] * len(nums)
        flips_past_window = 0
        res = 0

        for i in range(len(nums)):
            if i>=k:
                if flipped[i-k]:
                    flips_past_window -= 1
            
            if flips_past_window % 2 == nums[i]:
                if i+k > len(nums):
                    return -1
                
                flips_past_window += 1
                flipped[i] = True
                res += 1
        
        return res
