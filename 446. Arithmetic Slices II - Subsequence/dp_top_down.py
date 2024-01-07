"""
Pick 2 numbers from nums and then try to get the next valid number.
The next valid number is nums2 + diff of nums2 and nums1.
Use top down dp to avoid repeated work.
Run a loop from 0 -> len(nums)-2 and another loop inside it from i+1 -> len(nums)-1.
These are the 2 numbers which form the basis of the sequence, diff is nums[j] - nums[i] and next valid number is nums[j] + diff.
To get the possible combinations from this, add the result of the helper function.
The helper function takes in the last index, which is j at start and the diff.
Base case if last index == len(nums), this means we cannot add more and return 0.
Iterate through the nums after j, if the next number exists, call the recursive function and add 1 since this is a valid solution.
Memoization on (last index, diff).
Optimize the search for the next element by storing the numbers and their indexes in a hashmap.
This hashmap has key as the number and value is a list of indexes where they are found.
So instead of iterating from j and going over all numbers, simply go through the indexes of that number from the hashmap. Make sure to accept the only when the index > last index.

O(n^2) time. Im not sure.
O(n^2) space, im not sure. 
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        positions = collections.defaultdict(list)
        for i,n in enumerate(nums):
            positions[n].append(i)
        
        memo = {}
        def helper(last_idx, diff):

            if (last_idx, diff) in memo:
                return memo[(last_idx, diff)]

            if last_idx == len(nums):
                return 0

            total = 0
            next_number = nums[last_idx] + diff
            if next_number in positions:
                for k in range(len(positions[next_number])):
                    next_number_idx = positions[next_number].pop(k)
                    if next_number_idx > last_idx:
                        total += helper(next_number_idx, diff) + 1
                    positions[next_number].insert(k, next_number_idx)
            
            memo[(last_idx, diff)] = total
            return total

        res = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                diff = nums[j] - nums[i]

                res += helper(j, diff)

        return res
