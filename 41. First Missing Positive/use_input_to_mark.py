"""
3 pass solution using input array to mark numbers.
Due to the nature of the problem, we can see that the solution exists in the range [1, n+1].
This is because if we have an array [1,2,3,4,5], we have ALL positive integers from 1 to 5, thus the first missing pos integer will be 6, which is n+1.
On the other end, if we have [2,3,4], then the first positive integer is 1.
We do not care about negative numbers and we need to handle them.
Thus this way we can use the input array to mark elements as present. We dont care about a case where arr = [10,11], because 10 is > n+1, and will NEVER be the solution and thus we dont need to mark it.
First Pass: set all negatives to 0.
Second pass, for each element, get its index as abs(x)-1 and negate it to mark it present. If an element is already negated, this means we already saw it and dont need to negate again.
Also for an element == 0, set it to -1 * (n+1), this is because n+1 is the max value we could ever have as the solution, so it wont interfere with the solution.
Also make sure to only do it for numbers in the range [0, n].
Third Pass: Now iterate from 1 -> n+1, check the element at nums[i], return i as soon as we see a pos integer, this will be the first positive missing integer.
If we go through this loop and dont return, this means the solution is n+1.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # pass 1, set all negatives to 0
        for i,n in enumerate(nums):
            if n < 0:
                nums[i] = 0
        
        # pass 2, set the element's index to negative to mark it is present. nums[abs(x)-1] to get the corresponding index. Make sure it is in bound [0, n)
        for n in nums:
            idx = abs(n)-1
            if 0 <= idx < len(nums):
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                elif nums[idx] == 0:
                    nums[idx] = -1 * (len(nums)+1)
        
        # pass 3, iterate from 1 -> n+1, return as soon as we find a positive element
        for i in range(1, len(nums)+1):
            idx = i-1
            if nums[idx] >= 0:
                return i
        
        return len(nums)+1
