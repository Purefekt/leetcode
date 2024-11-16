"""
Get the largest non dec array left to right called left.
Get the largest non inc array right to left called right.
If left array the same size as arr, return 0.
Now we have 2 sorted arrays, we need to try to combine them.
Place a pointer at the start of both.
Suppose arr = [1,2,3,10,4,2,3,5]
left = [1,2,3,10]
right = [2,3,5]
If l = 0 and r = 0 is valid, ie left[l] <= right[r], this means we are using 1 item from left and all of right.
If l = 2 and r = 1 is valid, this means we are using 3 items from left and all except the 1st item of right.
First move r till we get the first valid state, save this size.
And then increment left and try again.

O(n) time for 2 passes to build left and right and then one pass using two pointers.
O(n) space used by left and right arrays.
"""

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        # get longest non dec array from left side
        left = []
        cur = -1
        for n in arr:
            if n < cur:
                break
            left.append(n)
            cur = n
        
        if len(left) == len(arr):
            return 0
        
        # get longest non dec array from right side
        arr = arr[::-1]
        right = []
        cur = math.inf
        for n in arr:
            if n > cur:
                break
            right.append(n)
            cur = n
        right = right[::-1]

        # try to merge both arrays
        keep_size = 0
        l = 0
        r = 0
        while l<len(left) and r<len(right):
            while r < len(right) and left[l] > right[r]:
                r += 1
            keep_size = max(keep_size, l + (len(right)-r) + 1)
            l += 1
        
        return len(arr) - max(keep_size, len(left), len(right))
