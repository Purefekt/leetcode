"""
Backtracking.
We need to split at operators. Dont think about where to place parenthesis but think of what they do.
If we have 2*3-5, we can either get 2*(3-5) or (2*3)-5.
We split at the * and then at the -.
First convert input into an array of integers and operators. 2*3-5 becomes [2,*,3,-,5].
Backtracking function takes an array.
If the size of array is 1, return the array. If arr = [2], we return [2].
If size of array if 3, return the output of performing the action, the 2nd element will be the operator. [2,*,3] will return [6].
Init an empty array and iterate through the array. If any arr[i] is an operator, we can split here.
Left will be backtrack(arr[:i]) and right will be backtrack(arr[i+1:]).
We will recieve 2 arrays. We need to get an array of all possible answers using that operator.
Suppose we split on operator = *. Left = [2] and right = [-2] (3-5).
We will get [-4].

O(n*2^n) time. For each array of size n, we find where to split it. For split, we have 2 paths, left and right.
O(2^n) space used by result.
"""

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        # create array of numbers and operators
        ops = {'*', '-', '+'}
        arr = []
        num = ""
        for c in expression:
            if c in ops:
                arr.append(int(num))
                arr.append(c)
                num = ""
            else:
                num += c
        if num:
            arr.append(int(num))
        
        def helper(nums):
            if len(nums) == 1:
                return nums
            if len(nums) == 3:
                if nums[1] == '+':
                    return [nums[0]+nums[2]]
                elif nums[1] == '*':
                    return [nums[0]*nums[2]]
                elif nums[1] == '-':
                    return [nums[0]-nums[2]]
            
            res = []
            # break at an operator
            for i in range(len(nums)):
                if nums[i] in ops:
                    left = helper(nums[:i])
                    right = helper(nums[i+1:])
                    for op1 in left:
                        for op2 in right:
                            if nums[i] == '+':
                                res.append(op1+op2)
                            elif nums[i] == '*':
                                res.append(op1*op2)
                            elif nums[i] == '-':
                                res.append(op1-op2)
            return res
                        
        return helper(arr)
