"""
Greedy.
We can only modify once.
Iterate through the array and compare each pair of numbers.
If i > i+1, now we need to modify. If we have already modified before, then return False.
If we havnt modified yet, then we need to change either i or i+1.
If i+1 >= i-1, then we set i = i+1, this is because we want to minimize it as much as possible. [1,4,2,1], if we are at index 1, then we will change index 1 = 2 => [1,2,2,1].
Else we need to set i+1 to i to maintain non decreasing order. [3,4,2,3], if we are at index 1, then we will change index 2 = 4 => [3,4,4,3].
Also edge case if index == 0, then simply change i to i+1 since we dont have i-1.
And change modified to True.

O(n) time to go through the array once.
O(1) space.
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        modified = False

        for i in range(len(nums)-1):
            # if its valid, then continue
            if nums[i] <= nums[i+1]:
                continue

            # all cases here are when current element is > next element
            # if already modified, then cannot modify again
            if modified is True:
                return False
            
            # Since we havnt modified anything yet, we can either modify i or i+1.
            # ideally we want to modify i to i+1, since i+1 is smaller value, which will help in a non increasing setting.
            # But if i-1th element is larger than i+1, then we need to modify i+1 to i.
            if i==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            modified = True
        
        return True
            