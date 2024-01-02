"""
Get the frequency of each number in nums.
The highest value will be the number of rows needed in the 2d array.
Create a result array with those many empty rows.
For each kv pair in frequency, append the key to v number of different bucket arrays.

O(n) time since there are n numbers.
O(n) space for counter hashmap.
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        num_rows = 0
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
            num_rows = max(num_rows, freq[n])
        
        res = [[] for i in range(num_rows)]
        
        for k,v in freq.items():
            for i in range(v):
                res[i%num_rows].append(k)
        
        return res
