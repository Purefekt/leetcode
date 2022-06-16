"""
perform the operation and check if the sum is 1. If not, add this sum to the hashset and repeat on this new num. If a new sum is already in the hashset, then we have a cycle.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        # create a hashset of sum of squares
        hashset = set()
        
        while(1):
            
            curr_sum = 0
            for num in str(n):
                curr_sum = curr_sum + (int(num) * int(num))
            
            if curr_sum == 1:
                return True
            
            if curr_sum in hashset:
                return False
            
            # add curr_sum to hashset:
            hashset.add(curr_sum)
            
            # update n
            n = curr_sum
            