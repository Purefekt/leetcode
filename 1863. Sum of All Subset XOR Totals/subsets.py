class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        def helper(idx, combo):
            nonlocal res

            if idx == len(nums):
                vals = combo.copy()
                if not vals:
                    res += 0
                else:
                    to_add = vals[0]
                    for i in range(1, len(vals)):
                        to_add ^= vals[i]
                    res += to_add
                return
            
            # skip
            helper(idx+1, combo)
            # keep
            combo.append(nums[idx])
            helper(idx+1, combo)
            combo.pop()
        
        helper(0, [])
        return res
