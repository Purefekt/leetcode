"""
Start with low number, try to sequential numbers using it.
First check that the first digit (left most) + len(number) - 1 < 10.
This means, 100 is valid, since we can make 123, but 800 is invalid, since we cant make 890.
For each number find all sequantial digits and add it to the solution, break if at any point a sequence > high.
Once it is done for all of the same size, suppose we are done with 12,23,34,45,56,67,78,89, now we need to move to 3 digits.
Make all numbers 0, append a 0 at end and set first to 1 and repeat, thus we repeat from 1000.

O(1) time since the loop to create pairs can run for at max 10 times and the loop at add the digit runs for at max 9 times since high is up to 10^9.
O(1) space, the largest number can be is 9 digits.
"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        cur_list = [c for c in str(low)]
        cur_num = low

        res = []
        while cur_num <= high:
            while int(cur_list[0]) + len(cur_list)-1 < 10:
                for i in range(1, len(cur_list)):
                    cur_list[i] = str(int(cur_list[i-1]) + 1)
                cur_num = int(''.join(cur_list))
                if cur_num > high:
                    break
                if low <= cur_num <= high:
                    res.append(cur_num)
                cur_list[0] = str(int(cur_list[0]) + 1)
            
            # add another digit to the number
            for i in range(len(cur_list)):
                cur_list[i] = '0'
            cur_list[0] = '1'
            cur_list.append('0')
            cur_num = int(''.join(cur_list))
        
        return res
                