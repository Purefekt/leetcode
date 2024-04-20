class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        min_sum = math.inf
        cur = 0
        
        for n in nums:
            cur += n
            min_sum = min(min_sum, cur)
        
        if min_sum >= 0:
            return 1

        if -min_sum + 1 == 0:
            return 1
        return -min_sum + 1
