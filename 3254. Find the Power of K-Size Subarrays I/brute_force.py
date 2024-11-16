"""
Brute force since contraints are low.
Solve part 2 for harder contraints.

O(n*k) time
O(1) space
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        def power(arr):
            res = -1
            flag = True
            cur = arr[0]-1
            for n in arr:
                if n != cur+1:
                    flag = False
                    break
                cur = n
                res = max(res, n)
            if flag is False:
                return -1
            return res


        res = []
        for i in range((len(nums)-k)+1):
            p = power(nums[i:i+k])
            res.append(p)
        
        return res
