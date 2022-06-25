"""
Using iteration, storing the values. O(n) time.
"""

class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        # index of this array will be the answer
        store_vals = [0,1]
        
        for i in range(2,n+1):
            next_val = store_vals[-1] + store_vals[-2]
            store_vals.append(next_val)
        
        return store_vals[-1]
    