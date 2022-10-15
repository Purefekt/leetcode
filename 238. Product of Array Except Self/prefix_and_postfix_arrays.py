"""
Create prefix and postfix arrays. 
Prefix product of the first element is 1 and postfix product of the last element is 1.
prefix[i] = prefix product for element i
postfix[i] = postfix product for element i
O(n) time and space.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        # initialize prefix and postfix. prefix[0] = postfix[-1] = 1
        prefix = [0] * len_nums
        prefix[0] = 1
        postfix = [0] * len_nums
        postfix[-1] = 1
        
        # fill prefix and postfix
        for i in range(len_nums-1):
            prefix[i+1] = nums[i]*prefix[i]
        
        for i in range(-1, -len_nums, -1):
            postfix[i-1] = nums[i]*postfix[i]
        
        answer = [0] * len_nums
        for i in range(len_nums):
            answer[i] = prefix[i]*postfix[i]
        
        return answer
        