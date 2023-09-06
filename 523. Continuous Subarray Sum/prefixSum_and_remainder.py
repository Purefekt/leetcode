"""
Get the prefix sum of the array and then get the mod with k of each index of the prefix sum.
This is the array of the remainders of prefix sum array.
If there are 2 remainders which are the exact same, this means that we have a multiple of k in between them.
For example [23, 2, 4] -> [23, 25, 29] and if k=6 -> [5, 1, 5]. The 0th and 2nd index are 23 and 29 and if we do 29-23, we get 6. This could be any multiple of 6.
Thus is we have any 2 remainders which are the same, we have a subarray which is a multiple of k.
BUT, we also need to check if the subarray is atleast of length 2, so we need to maintain a hashmap of remainder and its index.
Whenever we encounter a previously seen remainder, we need to check if this index is atleast >= 2, if yes then return True.
If we dont find any then return False.
An edge case is when the entire remainder array is unique but a single remainder is 0. To solve this, we initialize remainder hashmap with 0:-1, so that if the first element itself is a multiple of k, it wont satisfy the condition since 0 - -1 == 1, which is not >= 2. And if the element is not the first, for example if it is 4th, then it will satisfy the condition, since 4- -1 == 5 which is >= 2.

O(n) time to iterate through the nums array once.
O(n) space to store the remainder array which could have all unique remainders, making its size at max k which is at max n.
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder = {0:-1}

        total = 0
        for i, n in enumerate(nums):
            total += nums[i]
            rem = total % k

            if rem not in remainder:
                remainder[rem] = i
            else:
                if i - remainder[rem] >= 2:
                    return True
        
        return False
        