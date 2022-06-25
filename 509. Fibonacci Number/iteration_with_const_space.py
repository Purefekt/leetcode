"""
Iteration using constant space. Only keep n-1 and n-2 at a time. when calculating a new value, overwrite n-2 with n-1 and n-1 with new n-1.
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        n_1 = 1
        n_2 = 0
        
        for i in range(2, n+1):
            temp_n_1 = n_1
            
            n_1 = n_1 + n_2
            n_2 = temp_n_1
        
        return n_1
        