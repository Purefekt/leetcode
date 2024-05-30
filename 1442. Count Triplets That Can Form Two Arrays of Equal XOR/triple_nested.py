"""
Brute force.
Triple nested loop, i goes from 0 till n-1.
j from i+1 till n.
k from j till n.
Init a_xor in i loop and update in j loop to ^= arr[j-1].
Init b_xor in j loop and update in k loop to ^= arr[k].
Compare and update res.

O(n^3) time for tripled nested loop.
O(1) space.
"""

class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        res = 0
        for i in range(len(arr)-1):
            # init x_xor
            a_xor = 0
            for j in range(i+1, len(arr)):
                a_xor ^= arr[j-1]
                # init b_xor
                b_xor = 0
                for k in range(j, len(arr)):
                    b_xor ^= arr[k]

                    if a_xor == b_xor:
                        res += 1

        return res
                    