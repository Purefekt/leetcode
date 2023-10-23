"""
Sliding window.
Start sliding window with l=0 and r=1.
Maintain a flag, is the flag is None, this means the flag hasnt been set and can be set to either.
If flag is False, this means the next element must be smaller.
If flag is True, this means that next element must be greater.
Increment the right pointer to get the max subarray. Reset to l = r-1 any time the condition is not met.

O(n) time to go over all elements at most once.
O(1) space to store l,r and flag
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        l = 0
        r = 1
        res = 1

        # None means not set. True next must be greater. Flase means next must be smaller.
        flag = None
        while r < len(arr):
            if flag is None:
                if arr[r] == arr[r-1]:
                    flag = None
                    l += 1
                    r += 1
                elif arr[r] < arr[r-1]:
                    flag = True
                    r += 1
                    res = max(res, r-l)
                else:
                    flag = False
                    r += 1
                    res = max(res, r-l)
            
            elif flag is True:
                if arr[r] > arr[r-1]:
                    r += 1
                    res = max(res, r-l)
                    flag = False
                else:
                    l = r-1
                    flag = None
            
            else:
                if arr[r] < arr[r-1]:
                    r += 1
                    res = max(res, r-l)
                    flag = True
                else:
                    l = r-1
                    flag = None
        
        return res
