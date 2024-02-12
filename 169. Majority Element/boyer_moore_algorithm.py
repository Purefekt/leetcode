"""
Boyer-Moore voting algorithm. 
This only works if it is gauranteed that there is a majority element in the array.
Create majority candidate and count variables.
Iterate through the array.
If the count is 0, this means we can start tracking the current element as the majority candidate.
If we see an element == candidate element, we increment the count, otherwise we decrement it.
As soon as the count reaches 0 again, we change the candidate element.

O(n) time.
O(1) space.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = None
        count = 0

        for n in nums:
            if count == 0:
                count += 1
                res = n
                continue
            
            if n == res:
                count += 1
            
            else:
                count -= 1
        
        return res
