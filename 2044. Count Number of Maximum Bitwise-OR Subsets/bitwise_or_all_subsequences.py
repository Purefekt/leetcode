"""
Max bitwise or is the bitwise or of the entire array.
Get the bitwise or of each subsequence, if it is the max bitwise or, then increment result.

O(2^n) time where n is the size of nums. Since we can either choose to keep a num in a subsequence of skip it. Causing a branching factor of 2 and height of tree will be n.
O(n) space used by stack.
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        max_bo = 0
        for n in nums:
            max_bo |= n
        
        # get bitwise or for all subsets
        def helper(idx, bitwise_or):
            if idx == len(nums):
                if bitwise_or == max_bo:
                    return 1
                else:
                    return 0
            
            res = 0
            # use this num
            new_bitwise_or = bitwise_or | nums[idx]
            res += helper(idx+1, new_bitwise_or)
            # dont use it
            res += helper(idx+1, bitwise_or)

            return res

        return helper(0, 0)

