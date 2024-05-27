class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()

        flag = False
        for x in range(1, 101):
            for j in range(len(nums)):
                if nums[j] >= x:
                    flag = True
                    break
            
            if flag:
                if len(nums)-j == x:
                    return x
        
        return -1
