"""
Insertion sort.
Fix the first num in the result, starting from the 2nd num till the end, place it into the result list in its correct sorted position.
If we have [9,5,30], at first res = [9], then we take 5 and we see if we place it to the left of 9 or to the right, and get [9,5], then we take 30 and see where to place it and get [9,5,30]
Each time we take a number from nums, we compare it to all the numbers in the sorted result array left to right. To check this we make the 2 possible combinations, place nums to left of res or to the right
If we find a combination where left is greater, we know it is greater than every single remaining number in result, so we stop

O(n^2) time. To compare each number with every other number
O(n) space to store result array
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # insertion sort
        res = [str(nums[0])]

        for i in range(1,len(nums)):
            j = 0
            while j<len(res):
                left_side = str(nums[i]) + res[j]
                right_side = res[j] + str(nums[i])
                if left_side >= right_side:
                    break
                j += 1

            res.insert(j, str(nums[i]))
        
        res_number = int(''.join(res))
        return str(res_number)
