"""
Kind of binary search on a binary tree.
Suppose n=4, this means the last level of tree will have 8 nodes and we need to find the value of kth index.
Lets say the indexes are 1,2,3,4,5,6,7,8 and k=6.
Start with 0th node and set l=0 and r=8, split the search space into [0:4], [5,8] now if we go left we will never find k, so we must go right.
If we go right, the node value changes.
And if we left, it does not.
Repeat this n-1 times to reach the last level.

O(n) time since we need to go n-1 levels deep.
O(1) space since we use pointers to specify the search space.
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        l = 1
        r = 2**(n-1)
        cur = 0
        for i in range(n-1):
            m = (l+r)//2
            left = [l, m]
            right = [m+1, r]

            if l <= k <= m:
                # go left
                r = m
                # going left doesnt change cur
            else:
                # go right
                l = m+1
                if cur == 0:
                    cur = 1
                else:
                    cur = 0
        
        return cur
