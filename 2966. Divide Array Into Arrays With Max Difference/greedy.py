"""
Greedy.
Sort the array and try to make all sets of 3 elements.
If at any point the difference between last and first points is > k, return [], this cant be done.
Else add the current subarray to result and continue.

O(nlogn) time to sort.
O(n) space to sort.
"""

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()

        start = 0
        end = 2
        res = []
        for i in range(len(nums)//3):
            if nums[end] - nums[start] > k:
                return []
            else:
                res.append(nums[start:end+1])
                start = end+1
                end = end+3
        
        return res
