"""
Start from the right end and keep track of which number we are checking duplicates for and its count.
Initially set checking to nums[-1], means we are checking for duplicates of nums[-1] number and its count is 0.
Start from len(nums)-1 index and increment count if we see the same number.
If we see a different number, set checking to that and set count to 1.
If the count > 2 at any point, create a new pointer at i and loop till len(nums)-1 and shift the numbers by 1 position to the left.
So set nums[j] to nums[j+1] in a loop where j in range(i, len(nums)-1).
Also use a counter for number of times we had to shift and return len(nums)-this number.

O(n^2) time since we do a loop from right to left and within each, we run a loop from ith till end.
O(1) space since we only use pointers and counters.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        checking = nums[-1]
        count = 0
        changes = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == checking:
                count += 1
                if count > 2:
                    changes += 1
                    # shift all numbers left from i+1
                    for j in range(i, len(nums)-1):
                        nums[j] = nums[j+1]
                    # since this occurance was removed, decrease count
                    count -= 1
            else:
                checking = nums[i]
                count = 1

        return len(nums) - changes
