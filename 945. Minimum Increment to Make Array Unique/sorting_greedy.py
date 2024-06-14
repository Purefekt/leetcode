"""
Sorting greedy.
If we sort and get all the unique keys and their counts.
We can start with the sorted order of unique keys, and keep track of the current minimum value.
ie the next value HAS to be larger than this.
Suppose we have [3,2,1,2,1,7], we get unique vals sorted [1,2,3,7] and their counts are [2,2,1,1].
We start with current min = -1.
Start with sorted unique vals, loop over its count, if cur_min < k, we dont need to change this but we will update cur_min to k.
If cur_min >= k, then we need to change this occurance of k to atleast cur_min, so we add cur_min - k to result and continue.

O(nlogn) time for sorting and then n time to get frequency and n time to iterate over counts of all keys.
O(n) space used by sorting and freq hashmap and unique keys.
"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        keys = sorted(list(freq.keys()))
        res = 0
        cur_min = -1
        for k in keys:
            for count in range(freq[k]):
                if cur_min < k:
                    cur_min = k
                else:
                    cur_min += 1
                    res += cur_min - k
        
        return res
