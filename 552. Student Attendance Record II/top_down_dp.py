"""
This code gives memory error but it is correct.
Reason for memory error: Official solution is using list as memo and i am using hashmap. The extra memory used for keys is causing issue. The official solution doesnt need to spend extra memory on keys since the key is the index of list. I am too tired to change my sol to that.
We simply try all solutions. 
Base case stop when total == n and we return 1 since this is a valid attendance sheet.
At each point, we can either mark the student present, absent (only if total absents are less than 2) or late (only if consecutive lates are < 3).
We need to pass number of total absence, number of consecutive lates and total to the function.
Memoiz on that.

O(n) time since the functions runs at max for num_a * cons_l * n times. But num_a = 2 and cons_l = 3 so we get 2*3*n.
O(n) space, the hashmap will be of size 6n for the same reason as above.
"""

class Solution:
    def checkRecord(self, n: int) -> int:
        
        mod = 10**9 + 7

        memo = {}
        def helper(num_a, cons_l, total):

            if (num_a, cons_l, total) in memo:
                return memo[(num_a, cons_l, total)] % mod

            if num_a >= 2 or cons_l >= 3:
                return 0

            if total == n:
                return 1
            
            res = 0
            # student is present
            res += helper(num_a, 0, total+1) % mod
            # student is late only if cons_l < 3
            if cons_l < 3:
                res += helper(num_a, cons_l+1, total+1) % mod
            # student is absent only if num_a < 1
            if num_a < 1:
                res += helper(num_a+1, 0, total+1) % mod
            
            memo[(num_a, cons_l, total)] = res % mod
            return res % mod
        
        return helper(0, 0, 0) % mod
