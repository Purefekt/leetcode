"""
Save the initial array as as and also as a prefixSum.
[1,3] saved as [1,4].
Here all indexes of [0:1] go to 1 and all indexes [2:4] go to 3.
For pickIndex, use a random number generator in the range (1, prefixSum[-1]) inclusive.
Run linear search over the prefixSum array to find the correct index.
Optimize it by using binary search over the array instead.

O(n), O(logn) time. Constructor takes linear time to create prefixsum and pickIndex runs in logn time. Random number generator is O(1).
O(n), O(1) space. Constructor takes linear space for prefixSum array and pickIndex runs in constant time.
"""

class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [w[0]]
        for i in range(1, len(w)):
            self.prefixSum.append(self.prefixSum[i-1] + w[i]) 

    def pickIndex(self) -> int:
        # get a random number in the range [1, self.prefixSum[-1]]
        random_choice = random.randint(1, self.prefixSum[-1])

        # get the number at this index using binary search
        l = 0
        r = len(self.prefixSum)-1

        while l<=r:
            p = (l+r)//2

            if self.prefixSum[p] == random_choice:
                return p
            elif self.prefixSum[p] > random_choice:
                r = p-1
            else:
                l = p+1
        
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()