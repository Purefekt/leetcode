"""
Binary search. We have 2 sorted arrays. One ascedning and one descending. 
Run binary search, if the pivot is less than its next element, it must mean the largest element is to the right.
else the pivot is larger than the next element, in which case the largest element is on the left side

O(log(n)) time
O(1) space
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 0
        r = len(arr)-1
        
        while l<r:
            p = (l+r)//2
            
            if arr[p] < arr[p+1]:
                l = p+1
            else:
                r = p
        
        return l
    