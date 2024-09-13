"""
Prefixsum xor.
Create a psum array of xor from arr.
To find query[l,r] -> we can use the psum array in this way psum[r] ^ psum[l-1].
Except for when l==0, it is simply psum[r].

P(n+q) time where n is size of arr and q is size of queries since we do 2 separate loops.
O(n) space used by psum array.
"""

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        psum = []
        cur = 0
        for a in arr:
            cur ^= a
            psum.append(cur)
        
        res = []
        for l,r in queries:
            if l == 0:
                res.append(psum[r])
            else:
                res.append(psum[r]^psum[l-1])
        
        return res
