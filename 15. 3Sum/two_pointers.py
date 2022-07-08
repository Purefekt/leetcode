"""
sort the input list
run a for loop over the sorted list.
use two pointers high and low. low will start at i+1 and high will start at len(nums)-1
check the sum of all three i,low,high. If the sum is 0, then add that tuple to a hashset(to avoid duplicates).
If the sum is lower, the increment the low pointer, if the sum is higher then decrement the high pointer
O(n^2) time
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort nums
        nums.sort()
        
        output = set()
        for i in range(len(nums)):
            low = i+1
            high = len(nums)-1
            
            while low<high:
                if nums[i]+nums[low]+nums[high] == 0:
                    triplet = (nums[i], nums[low], nums[high])
                    output.add(triplet)
                    low += 1
                elif nums[i]+nums[low]+nums[high] < 0:
                    low += 1
                elif nums[i]+nums[low]+nums[high] > 0:
                    high -= 1
        
        output = list(output)
        return output
    