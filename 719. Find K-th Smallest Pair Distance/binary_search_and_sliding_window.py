"""
Binary search + sliding window.
The max distance can be max(nums) - min(nums).
We can binary search over distance.
For a given distance, find number of pairs whose absolute distance <= current distance.
If the number of such pairs < k, we need to search to the right of this distance, else we search to the left of it.
To efficiently get the number of pairs whose distance <= current distance, we can sort the array.
Use a left and right pointer and use sliding window. Keep expanding the window while valid, for each, we add right-left to number of pairs.
Since all numbers till right-1 form pairs with left num whose distance <= current distance.
If at any point nums[right] - nums[left] > current distance, we need to shift left till this statement is invalid aka fix the window.

O(nlogn + nlogm) time where n is the size of nums and m is max(nums) - min(nums). nlogn comes from sorting and logm comes from binary search over m, for which we count number of pairs in n time.
O(n) space used by sorting.
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        # binary search over 0 and max possible distance
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid_dis = (low+high)//2

            # for this distance, find the number of pairs whose distance <= this. Do this with sliding window
            num_pairs = 0
            left = 0
            right = 0
            for right in range(len(nums)):
                # adjust left to keep absolute distance in range
                while nums[right] - nums[left] > mid_dis:
                    left += 1
                num_pairs += right - left
            
            # if number of pairs are < k, this means distance must be larger than mid_dis
            if num_pairs < k:
                low = mid_dis + 1
            else:
                high = mid_dis
        
        return low
