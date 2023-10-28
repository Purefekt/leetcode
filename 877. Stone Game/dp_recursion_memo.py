"""
DP. Recursion with memo.
At each step, a player can have 2 choices, either to take left most or right most.
Find alice's max total this way.
Helper function takes (l,r) and thus we have n^2 possibilities since l can be of size n and r can be of size n.
If we choose left, then we add piles[l] and call helper(l+1, r).
If we choose right, then we add piles[r] and call helper(l, r-1).
Base case return 0 if l>r.
We do not care about Bob's total, so if it is bob's turn, simply return 0 since it wont add to alice's total.
To determine if its bob's turn, check if the range is odd (r-l+1). If even range, means it is alice's turn.

O(n^2) time since we have l*r computations.
O(n^2) space to store n^2 records in hashmap
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def helper(l, r):
            if (l,r) in memo:
                return memo[(l,r)]

            if l>r:
                return 0
            
            # if num of remaining options is even, this means alice is choosing, else bob is choosing
            num_remaining = r-l+1
            even = False
            if num_remaining % 2 == 0:
                even = True
            
            left = 0
            right = 0
            if even is True:
                left = piles[l]
                right = piles[r]
            
            res = max(left + helper(l+1, r), right + helper(l, r-1))
            memo[(l,r)] = res
            return res
        
        alice_total = helper(0, len(piles)-1)
        if alice_total >= math.ceil(sum(piles)/2):
            return True
        return False
