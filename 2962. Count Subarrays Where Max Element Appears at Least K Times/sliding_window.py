"""
Sliding window maintaining the count of max element seen so far.
Shift the right till we get count of max element == k.
As soon as we do, shift the left till just after count = k-1.
This means for any subarray which ends at r, can start at all indexes from 0 till l-1 and be a valid subarray.
Eg: [1,3,2,3,3]. We shift r till index 3. Now we have count == 2. We shift l till index 2.
Now we know that if we start at index 0 or index 1 and end at index 3, both these subarrays are valid and increment answer by 2 which is l.
Next we shift right to index 4. We shift left to 4 as well and we know that indexes 0,1,2,3 are valid if we end at index 4, thus add 4 to the result which is l.

O(n) time for sliding window.
O(1) space.
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        res = 0
        val = max(nums)
        l = 0

        freq = 0
        for r in range(len(nums)):
            if nums[r] == val:
                freq += 1
            while freq == k:
                if nums[l] == val:
                    freq -= 1
                l += 1
            
            res += l
                
        return res
