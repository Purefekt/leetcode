"""
Greedy.
If the left neighbhor is less than num and its right neighbhor is greater than num (or vice versa), then there is a possibility that their average == num.
To gaurantee that the average will never be the num is if both the left and right neighbhors are either less than or greater than num.
Sort the nums and take the first half of them and place them in all odd spots in the result array.
Place the second half in the event spots in the result array.

O(nlogn) time. for sorting. Building the result array takes O(n) time.
O(n) space for sorting.
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        nums.sort()

        res = [None] * len(nums)

        idx = 0
        for i in range(math.ceil(len(nums)/2)):
            res[idx] = nums[i]
            idx += 2
        
        idx = 1
        for i in range(math.ceil(len(nums)/2), len(nums)):
            res[idx] = nums[i]
            idx += 2
        
        return res
