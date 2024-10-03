"""
Psum solution and use mod to check for smallest array to remove.

O(n) time
O(n) space
""" 

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        to_remove = 0
        for n in nums:
            to_remove += n
            to_remove %= p
        
        if to_remove == 0:
            return 0
        
        hashmap = {0:-1}
        res = len(nums)
        cur = 0
        for i,n in enumerate(nums):
            cur += n
            cur %= p
            needed = (cur - to_remove + p) % p
            if needed in hashmap:
                res = min(res, i-hashmap[needed])
            hashmap[cur] = i
        
        return -1 if (res == math.inf or res == len(nums)) else res
