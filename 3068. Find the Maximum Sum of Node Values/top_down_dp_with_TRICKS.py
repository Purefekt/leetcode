"""
Trick: We can assume any 2 random nodes (adjacent or non adj) to simply be connected. This is because we have a undirected tree which means this is acyclic and there is a path from any node u to another node v.
Suppose we have u-p1-p2-v. Now if we perform the operation on all these pairs, we will have u^k, p1^k^k, p2^k^k and v^k. We get 2x XOR k for the middle nodes since we perform this operation on all pairs.
Property of xor is that A^B^B will simply result in A. Thus when we perform the operation on all edges in u-p1-p2-v, we get that nums[u] = u^k, nums[p1] = p1, nums[p2] = p2, nums[v] = v^k
Only u and v are affected and p1 and p2 are not.
This makes the edges input irrelevent to us.
Trick: Since this operation is performed on pairs, we can only perform this operation even number of times.
Now we can formulate the top down recursive function, it takes index and a boolean value which tells if the number of times op was performed is even or odd.
For each index, we can either xor where we add nums[idx]^k to it or we skip it which means we simply add nums[idx] to it.
Memoiz on this.

O(n) time for n nodes since the recursive function runs for n*2 times sine op_performed can be either 0 or 1.
O(n) space since the call stack will be of size 2*n.
"""

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        memo = {}
        def helper(idx, op_performed):
            if (idx, op_performed) in memo:
                return memo[(idx, op_performed)]

            if idx == len(nums):
                if op_performed % 2 == 0:
                    return 0
                else:
                    return -math.inf
            
            # xor this number
            xor_done = (nums[idx] ^ k) + helper(idx+1, (op_performed+1)%2)
            # skip this number
            skipped = nums[idx] + helper(idx+1, op_performed)
            memo[(idx, op_performed)] = max(xor_done, skipped)

            return memo[(idx, op_performed)]
        
        return helper(0, 0)
        