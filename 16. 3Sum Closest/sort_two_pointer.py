"""
Sort and two pointer.
Sort the array, now iterate over the elements from 0 till n-2
For each iteration, set a l pointer at i+1 and r pointer at n-1
Get the sum of the 3 numbers at i,l,r and update the closest variable based on absolute values. 
If the sum is greater than the target, we need to make it smaller and thus we move r pointer inside, else we move l pointer outside

O(n^2) time. O(nlogn) to sort and for each iteration, we run the 2 pointer solution, since it is nested and both are O(n), we get n^2
O(n) space to sort in python
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest = inf

        for i in range(0, len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l<r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if abs(target-cur_sum) < abs(target-closest):
                    closest = cur_sum
                
                if cur_sum <= target:
                    l += 1
                else:
                    r -= 1
            
        return closest
