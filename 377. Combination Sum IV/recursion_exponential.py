class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def helper(cur_sum):
            if cur_sum >= target:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            res = 0
            for n in nums:
                cur_sum += n
                res += helper(cur_sum)
                # backtrack
                cur_sum -= n
            
            return res
        
        return helper(0)
        