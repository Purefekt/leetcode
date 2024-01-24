class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0]
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            prefix.append(cur)
        prefix.append(0)

        total = prefix[-2]

        for i in range(1, len(prefix)-1):
            left = prefix[i-1]
            right = total - prefix[i]

            if left == right:
                return i-1
       
        return -1
