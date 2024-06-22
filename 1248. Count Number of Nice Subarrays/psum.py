"""
Prefixsum.
Get the prefixsum of number of odd numbers seen so far for the array.
Then iterate through the array, for each n in psum, if n-k existed already, then add the count of n-k to result.
This is because the count of n-k is the total number of valid subarrays we can make from n.
To do this, maintain a hashmap of count of n. Initialize it with 0 -> 1 since initially we have 0 odd numbers.

O(n) time to create psum and to iterate through psum array.
O(n) space used by frequency and psum data structures.
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        psum = []
        cur = 0
        for n in nums:
            if n%2 == 1:
                cur += 1
            psum.append(cur)
        
        freq = collections.defaultdict(int)
        freq[0] = 1
        res = 0
        for n in psum:
            if n-k in freq:
                res += freq[n-k]
            freq[n] += 1
        return res
