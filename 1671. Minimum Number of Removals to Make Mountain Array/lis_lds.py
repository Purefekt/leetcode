"""
LIS and LDS.
Since we are gauranteed a valid answer, we can find the pivot element with largest LIS on left side and largest LDS on right side.
Get the LIS of the array from left to right.
Get the LDS of the array from right to left.
Now for each element in range [1, n-1] since first and last elements are invalid.
Set this element as pivot and check what was the LIS from the left which ends at this element.
Then check what is the LDS to the right which starts at this element.
LIS[i] + LDS[i] - 1 is the size of such array. -1 since we are considering the pivot twice.
Also note that we need to check if both LIS[i] > 1 and LDS[i] > 1 because the min value can be 1.
And if either is 1, this means it is the start of the sequence or end of a sequence.
This means we are having a solution which either goes up like [1,2,3,4] or only goes down like [4,3,2,1].
Both of these are wrong since there needs to be a peak.

O(n^2) time to run LIS and LDS and get output.
O(n) space used by both arrays.
"""

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        # LIS from left to right
        lis = [1]
        for i in range(1, len(nums)):
            max_val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, lis[j])
            lis.append(max_val+1)

        # LDS from right to left
        lds = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            max_val = 0
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    max_val = max(max_val, lds[j])
            lds[i] = max_val + 1
        
        # set each index as pivot and get the max array. Subtract 1 since we use the pivot twice
        max_arr_size = 0
        for i in range(1, len(nums)-1):
            if lis[i] > 1 and lds[i] > 1:
                max_arr_size = max(max_arr_size, lis[i] + lds[i] - 1)
        return len(nums) - max_arr_size
