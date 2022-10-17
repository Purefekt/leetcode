"""
TWO POINTER
Sort the nums list
Iterate through the nums list. For each iteration set the left pointer to i+1 and right pointer to len(nums)-1
Run a while loop till l<r and check if the sum of nums[i] + nums[l] + nums[r] is 0
If 0, then add this to the result list and move the left pointer
If sum is negative, then move the left pointer, else move the right pointer
Also maintain a set to check if the given triplet has already been added to the result
O(n^2) time since we iterate through the list in O(n) time and for each iteration, we iterate the list for O(n-1) time. Sorting takes O(nlogn) time but O(n^2) is larger.
O(n) time due to sorting. res and res_set also take space less than n but not constant.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        res_set = set()
        nums.sort()
        
        for i, num in enumerate(nums):
            # if starting from the 2nd element, if it is same as the previous one, then skip
            if i>0 and num == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r:
                if num + nums[l] + nums[r] == 0:
                    if (num, nums[l], nums[r]) not in res_set:
                        res.append([num, nums[l], nums[r]])
                        res_set.add((num, nums[l], nums[r]))
                    l += 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            
        return res
    