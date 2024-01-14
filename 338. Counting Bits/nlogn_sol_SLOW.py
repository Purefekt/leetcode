"""
O(nlogn) solution.
For all numbers from 0 till n, run the following logic to get number of ones.
Start with the number, if num % 2 == 1, increment number of ones count by 1.
Then set the number = number // 2.
Repeat till number goes down to 0.

O(nlogn) time since it takes logn time for each number since we are decreasing it by a factor of 2 everytime, here log base 2. And we repeat it n times.
O(1) space.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        for i in range(n+1):
            num = i
            num_ones = 0
            while num != 0:
                if num % 2 == 1:
                    num_ones += 1
                num //= 2
            res.append(num_ones)
        
        return res
