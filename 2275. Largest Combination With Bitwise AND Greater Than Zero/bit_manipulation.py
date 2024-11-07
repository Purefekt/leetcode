"""
Since it is bitwise AND, we can calculate the number of nums we can use for each bit position for it to be 1.
For example if we have [1,2,3,4]
they are
001
010
011
100
in binary.
Now look at each column,
from right to left, bit 0 has 2x 1s.
bit 1 has 2x 1s.
bit 2 has 1x 1s.
This means we can have a combination of nums where we have 2 numbers and still have a value > 0.
To get the largest such combination, we can take 2 numbers from this combo.

O(n) time to iterate through candidates once. For each, we convert it to a string which wont be greater than 24.
O(1) space since the hashmap stores bit position and count, bit position is limited to 24.
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        # get count of number of 1 bits for each num
        count = collections.defaultdict(int)
        
        for num in candidates:
            binary = bin(num)[2:]
            # least sig bit is right most
            bit = 0
            for i in range(len(binary)-1, -1, -1):
                if binary[i] == '1':
                    count[bit] += 1
                bit += 1
        
        return max(count.values())
        