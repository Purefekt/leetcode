"""
Recursive solution with memoization
Maintain pointers for s1,s2,s3 -> p1,p2,p3
Explore the decision tree, if only s1[p1] == s3[p3] then we have 1 single path. Similarly if only s2[p2] == s3[p3] then we have 1 single path
But if both are same as s3[p3] then we can take 2 paths, we will use backtracking. Return True if we find any valid path ie when we reach the end of all s1,s2,s3
Cache the values for (p1,p2,p3) as True or False. The base case will be when p1==len(s1), p2==len(s2), p3==len(s3) : True
This will avoid us from visiting paths where we already computed the value

O(m*n) time. We can explore at most m*n nodes
O(m*n) space for memo
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = {(len(s1),len(s2),len(s3)):True}

        def backtrack(p1,p2,p3):

            if (p1,p2,p3) in memo:
                return memo[(p1,p2,p3)]
            
            if p1<len(s1) and p3<len(s3) and s1[p1] == s3[p3] and backtrack(p1+1, p2, p3+1) is True:
                memo[(p1+1, p2, p3+1)] = True
                return True
            if p2<len(s2) and p3<len(s3) and s2[p2] == s3[p3] and backtrack(p1, p2+1, p3+1) is True:
                memo[(p1, p2+1, p3+3)] = True
                return True
            
            memo[(p1,p2,p3)] = False
            return False
        
        return backtrack(0,0,0)
