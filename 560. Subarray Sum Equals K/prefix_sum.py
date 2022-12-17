"""
Prefixsum
Create a hashmap with the frequency of prefixsum. We will start with 0:1 since the sum 0 appears once by default even before starting the array
Go through the numbers and keep adding to the sum
On each iter, if sum-k is in hashmap, add the count of hashmap[sum-k] to count
Next if sum is not in the hashmap, add it with freq of 1 else increment by 1

O(n) time to go through all elements once
O(n) space to map n elements
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap = {0:1}
        
        count = 0
        summ = 0
        for n in nums:
            summ += n

            if summ-k in hashmap:
                count += hashmap[summ-k]
            
            if summ not in hashmap:
                hashmap[summ] = 1
            else:
                hashmap[summ] += 1
        
        return count
