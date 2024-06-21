"""
Prefix sum.
Get the prefix sum for grumpy without any magical minutes and prefixsum for customers.
We use a sliding window denoted by i and j to mark a window where all customers are happy.
Now we just need to get the number of customers which were satisfied as per normal execution in the left side of window and the right side of the window.
Using the prefix sum arrays, this becomes easier.

O(n) time.
O(n) space.
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        psum_grumpy = [0]
        psum_customers = [0]

        cur_g = 0
        cur_c = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                cur_g += customers[i]
            cur_c += customers[i]

            psum_grumpy.append(cur_g)
            psum_customers.append(cur_c)
        
        i = 1
        j = minutes
        res = 0
        while j < len(psum_grumpy):
            changed = psum_customers[j] - psum_customers[i-1]
            unchanged = psum_grumpy[-1]-psum_grumpy[j] + psum_grumpy[i-1] if j!=len(psum_grumpy)-1 else psum_grumpy[i-1]
            res = max(changed+unchanged, res)
            i += 1
            j += 1
        
        return res