"""
Prefix sum mod.
Get the mod k prefix sum of the array.
Also add a 0 at the start, for example for [1,2,3] k=2, we get psum as [0, 1, 3, 6] and psum mod k as [0, 1, 1, 0].
Now iterate through psum mod, and track the frequency of each number.
If a number exists in frequency, add its count to result and then increment 1.
If it does not exist, add the key value pair number, 1 to the hashmap.

O(n) time to build the psum array and one more pass over it.
O(n) space used by psum array and freq hashmap.
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        psum = [0]
        cur = 0
        for n in nums:
            cur += n
            psum.append(cur%k)
        
        freq = {}
        res = 0
        for n in psum:
            if n in freq:
                res += freq[n]
            else:
                freq[n] = 0
            freq[n] += 1
        
        return res
