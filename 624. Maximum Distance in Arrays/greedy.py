"""
Greedy.
Since we cant get both global min and global max from the same array, we need to track the global min/max and the second best.
Set max1 and min1 to global max and min.
Also track max2 and min2 as second best.
Keep the index since we need to make sure if they are from the same array.
Iterate through the array to get the max1, min1, max2, min2 = [value, index].
In the end, if index of min1 != max1, return their diff, simple case.
If the index is the same, we need to get the max of the diff between max1 - min2 and max2 - min1.

O(n) time to iterate through arrays once.
O(1) space.
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max1 = [-math.inf, None]
        max2 = [-math.inf, None]

        min1 = [math.inf, None]
        min2 = [math.inf, None]

        for i, arr in enumerate(arrays):
            if arr[-1] > max1[0]:
                # shift max1 to max2 status
                max2 = max1.copy()
                max1 = [arr[-1], i]
            else:
                if arr[-1] > max2[0]:
                    max2 = [arr[-1], i]
            
            if arr[0] < min1[0]:
                # shift min1 to min2 status
                min2 = min1.copy()
                min1 = [arr[0], i]
            else:
                if arr[0] < min2[0]:
                    min2 = [arr[0], i]
        
        if max1[1] != min1[1]:
            return max1[0] - min1[0]
        
        return max(
            max1[0] - min2[0],
            max2[0] - min1[0]
        )
