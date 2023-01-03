"""
Backtracking
Create a hashmap of counts of all numbers
Run backtracking as in permutations 1, but this time we iterate over the keys of the hashmap. 
We ONLY add the key to the permutation if its count is >0. When we add a key to a permutation, we decrement its value by 1
During cleanup, we not only pop from the permutation but also increment the value of that key

O(n!/prod(k!..)) n is the number of elements in our list. k is one of the element and the number of duplicates. So for the list [1,1,1,2,2,3,3], we will have 7!/(3!*2!*2!)
O(n) space for the recursion call stack and also hashmap.
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(perm, freq_hashmap):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for k in freq_hashmap.keys():
                # only if its count is > 0
                if freq_hashmap[k] > 0:
                    perm.append(k)
                    freq_hashmap[k] -= 1

                    backtrack(perm, freq_hashmap)

                    # cleanup
                    perm.pop()
                    freq_hashmap[k] += 1
            
        # get initial freq_hashmap
        freq_hashmap = {n:0 for n in nums}
        for n in nums:
            freq_hashmap[n] += 1
        
        backtrack([], freq_hashmap)
        return res
