"""
Divide and conquer.
2^10 can be 2^5 * 2^5.
2^5 can be 2^2 * 2^2 * 2.
2^2 can be 2 * 2.
Thus we need to calculate 2^2 once and 2^5 once to get the solution.
Recursive function takes x and abs(n).
Result = helper(x, n//2).
Result = result * result if x is even.
Result = result * result * x is x is odd.
Return 1/final result if n was negative, else just return.

O(logn) time.
O(1) space.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = helper(x, n//2)
            res = res * res
            if n % 2 == 0:
                return res
            else:
                return res * x
            
        
        res = helper(x, abs(n))

        if n < 0:
            return 1/res
        return res
