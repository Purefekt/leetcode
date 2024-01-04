"""
Since we can have sets of 2 or sets of 3 and we want to minimize operations, thus we need to maximize use of sets of 3s.
Edge cases, if frequency is 1 then return -1, if frequency is 2, we must use 1 operation.
Now, we can have at max 3 types of scenarios, suppose frequency of 3 numbers is 9, 10, 11.
For 9, optimal is 3 operations with 3 sets.
For 10, optimal is 4 operations, 2 of 3 sets and 2 of 2 sets.
For 11, optimal is 4 operations, 3 of 3 sets and 1 of 2 set.
This pattern repeats.

O(n) time to create hashmap and to iterate through it.
O(n) space to store hashmap.
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        res = 0
        for k,v in freq.items():
            if v == 1:
                return -1
            elif v == 2:
                res += 1
            else:
                if v%3 == 0:
                    res += v//3
                elif v%3 == 2:
                    res += v//3
                    res += 1
                elif v%3 == 1:
                    res += (v//3 - 1)
                    res += 2
        
        return res
