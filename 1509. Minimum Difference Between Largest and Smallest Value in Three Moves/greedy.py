"""
Greedy + sort.
Sort the nums.
Now delete 3 nums from any combination of 3 smallest and 3 largest.
We are deleting here which is the same as performing a move since when we change a number in this way, this number wont affect the difference between largest and smallest.

O(nlogn) time for sorting.
O(n ) space used for sorting. Actual calculation takes O(1) time.
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return 0
        
        nums.sort()
        # delete 3 nums from any combination of 3 smallest and 3 largest nums
        
        # delete all 3 from left
        op1 = nums[-1] - nums[3]
        # delete 2 from left and 1 from right
        op2 = nums[-2] - nums[2]
        # delete 1 from left and 2 from right
        op3 = nums[-3] - nums[1]
        # delete all 3 from right
        op4 = nums[-4] - nums[0]

        return min(op1, op2, op3, op4)