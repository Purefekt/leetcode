"""
Optimizing the prev solution to use constant space and 2 passes instead of 3
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        answer = [0]*len_nums
        
        # add prefix values to answer
        answer[0] = 1
        for i in range(len_nums-1):
            answer[i+1] = answer[i] * nums[i]
        
        # use postfix values and create final answer array
        postfix_i = 1
        for i in range(-1, -len_nums-1,-1):
            answer[i] = answer[i] * postfix_i
            postfix_i = postfix_i * nums[i]
        
        return answer
    