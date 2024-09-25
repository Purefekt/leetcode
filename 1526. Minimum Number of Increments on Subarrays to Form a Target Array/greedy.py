"""
Greedy.
Keep a variable prev which is the value of the previous cell.
Initialize prev to 0.
Iterate through the input, for an index where target[i] > prev, increment the diff.
Update prev to current element.
If we have [3,1,5,4,2], prev = 0.
On 0th index, we need 3 operations.
When we go to 1st index, we already have done 3 ops, and so we dont need any more ops, but now we update prev = 1.
Now when we go to 2nd index, we have already done 1 op, and need to do 4 more since 5-1 = 4.

O(n) time.
O(1) space.
"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        res = 0
        last_done = 0

        for i in range(len(target)):
            if target[i] > last_done:
                res += target[i] - last_done
            last_done = target[i]

        return res
