"""
Sort the input for easy iteration.
Create a hashmap which stores numbers from nums as key and the longest chain with that number at the end as value.
Iterate through nums, check if num is a perfect square.
If it is, check if the root of num exists in the hashmap.
If it does, then longest chain for num will be 1 + longest chain of root.
If it does not or if num isnt a perfect square, simply start a new chain by setting hashmap[num] = 1.

O(nlogn) time to sort and then n time to iterate over nums to get the result.
O(n) space for sorting and storing hashmap.
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums.sort()
        
        res = 0
        hashmap = {}
        print(nums)

        for n in nums:
            # check if n is a perfect square
            root = int(math.sqrt(n))
            if root * root == n:
                # if root doesnt exist in hashmap, start a new chain, else continue previous
                if root in hashmap:
                    hashmap[n] = hashmap[root] + 1
                    res = max(res, hashmap[n])
                else:
                    hashmap[n] = 1
            else:
                # not a perfect square, start a new chain
                hashmap[n] = 1
        
        return res if res != 0 else -1
