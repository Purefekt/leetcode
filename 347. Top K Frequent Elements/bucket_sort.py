"""
Bucket sort with trick.
Build the frequency hashmap of nums.
Now initialize a 2d list of size len(nums) + 1 with empty lists [] at each index.
An index in this list means all nums which have this frequency.
so for nums = [1,1,1,1,2,2,3,3], the 2d list is initialized as [[], [], [], [], [], [], [], []].
Then it is populated as [[], [], [2,3], [], [1], [], [], []].
Now iterate from right to left building result by extending the result with all nums.
Stop when len(res) == k.

O(n) time to build hashmap, then inverted freq and then iterating it.
O(n) space for storing all structures
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap for num -> its frequency in O(n) time
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # Build a inverted freq in O(n) time
        inverted_freq = []
        for _ in range(len(nums)+1):
            inverted_freq.append([])

        for key, val in freq.items():
            inverted_freq[val].append(key)
        
        # go from right end to left to get the k most frequenct nums
        res = []
        for i in range(len(inverted_freq)-1, -1, -1):
            if len(res) == k:
                break
            if inverted_freq[i]:
                res.extend(inverted_freq[i])
        return res
