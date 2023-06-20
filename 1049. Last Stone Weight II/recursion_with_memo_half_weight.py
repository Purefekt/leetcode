"""
To minimize the final stone weight, we need to find 2 subsets of stones, which are equal or as close to equal.
For example is total weight of stones is 24, if we can find 2 sets of size 12, then we can get a final weight of 0.
Thus we will try all combinations of stones to get the ceil(half of total sum) of stones.
The backtrack function will take the index and total sum thus far.
A basecase is if (idx, total) is in cache, then return.
Other basecase is if the total >= half or the index == len(stones), then we will return the weight we get by smashing these 2 subsets. For example if total sum is 23, then half is 12. If suppose we get a subset sum of 12, then we know the other subset is 11 and the final weight after smashing is abs(12-11) = 1.
For each stone, we decide to either keep the stone in this subset or not keep. And we will return the min of these 2 conditions.

O(n*stoneSum) time. We call the backtrack function idx * stoneSum/2 times at max.
O(n*stoneSum) space. Same as previous, used to recursion stack.
"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        stoneSum = sum(stones)
        half = math.ceil(stoneSum/2)

        memo = {}
        def backtrack(idx, total):

            if (idx, total) in memo:
                return memo[(idx, total)]

            if total >= half or idx == len(stones):
                memo[(idx, total)] = abs(total - (stoneSum - total))
                return memo[(idx, total)]
            
            memo[(idx, total)] = min(backtrack(idx+1, total), backtrack(idx+1, total+stones[idx]))
            return memo[(idx, total)]
           
        backtrack(0,0)
        return memo[(0,0)]
