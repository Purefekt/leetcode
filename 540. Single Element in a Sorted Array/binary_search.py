"""
Binary search.
All duplicate numbers will be next to each other.
Start binary search, check the number before pivot and after pivot. If either is true, then we found a pair, else return this number.
If we found pair, then calculate the number of integers to the left of pivots and to the right, the subarray with odd number of elements will contain the single number.

O(logn) time to execute binary search.
O(1) space to keep track of left, right, pivots
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)//2

            if p-1 >= 0 and nums[p-1] == nums[p]:
                p1 = p-1
                p2 = p

                if (p1-l) % 2 == 1:
                    r = p1-1
                else:
                    l = p2+1
                
            elif p+1 < len(nums) and nums[p+1] == nums[p]:
                p1 = p
                p2 = p+1

                if (p1-l) % 2 == 1:
                    r = p1-1
                else:
                    l = p2+1
            
            else:
                return nums[p]
