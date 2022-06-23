class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initialize the array
        result = []
        
        # take all non 0s and add them to the new array
        for n in nums:
            if n != 0:
                result.append(n)

        # fill the rest with 0s
        rem_zeros = len(nums) - len(result)
        
        for i in range(rem_zeros):
            result.append(0)
        
        # replace nums with result
        nums[:] = result
        