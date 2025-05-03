class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # get the first window
        cur = 0
        for i in range(k):
            cur += nums[i]
        res = cur / k

        # now iterate from kth index till the end and add from current and remove i-k
        for i in range(k, len(nums)):
            cur -= nums[i-k]
            cur += nums[i]
            res = max(res, cur/k)
        
        return res
