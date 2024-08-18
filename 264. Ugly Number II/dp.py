"""
An ugly number is always the multiple of 2 or 3 or 5.
And it is also a multiple of a previous ugly number.
We start at 1, with this we can get the ugly numbers 2,3,5. [1,2,3,5]
We take the next lowest = 2 and we can get 4,6,10. [1,2,3,4,5,6,10]
We take the next lowest = 3 and we can get 6,9,15. [1,2,3,4,5,6,6,9,15].
We need to dedupe and get [1,2,3,4,5,6,9,15]. But notice that we skipped 8.
We need to do this for all numbers till be have an array of size n, this will involve excess calculations.
We can use the knowledge of it being a multiple of 2,3,5 and it coming from a previous ugly number.
Start an array of size n and set res[0] = 1.
Set multi_2, multi_3, multi_5 = 2,3,5.
Set idx_2, idx_3, idx_5 = 0, this is the index in res to use to get the next multiple of that number.
Next number in array will be min(multi_2, multi_3, multi_5).
Since in the first iteration we have min(2,3,5), we set res[1] = 2.
We need to update multi_2 since it has been used. Set idx_2 += 1 and multi_2 = res[idx_2] * 2.
Repeat.

O(n) time.
O(n) space.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        multi_2 = 2
        idx_2 = 0
        multi_3 = 3
        idx_3 = 0
        multi_5 = 5
        idx_5 = 0

        res = [1]

        for i in range(1, n):
            next_num = min(multi_2, multi_3, multi_5)
            res.append(next_num)

            if next_num == multi_2:
                idx_2 += 1
                multi_2 = res[idx_2] * 2
            
            if next_num == multi_3:
                idx_3 += 1
                multi_3 = res[idx_3] * 3
            
            if next_num == multi_5:
                idx_5 += 1
                multi_5 = res[idx_5] * 5
        
        return res[-1]
