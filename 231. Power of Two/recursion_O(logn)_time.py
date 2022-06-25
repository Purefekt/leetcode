class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # edge case
        if n == 0:
            return False
        # base case
        if n == 1:
            return True
        
        if n % 2 == 0:
            return self.isPowerOfTwo(n/2)
        