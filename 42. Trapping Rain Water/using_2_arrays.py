"""
Find the amount of water trapped at each index
At a given index, the water we can trap is the min(max_left_bound, max_right_bound) - height[idx]
In the example, we can trap 0 water in idx 1 since the left bound is 0
In the example, we can trap 2 units at idx 5 since max_left is 2 and max right is 3, thus atleast 2 units can be trapped. That index itself has a height of 0 which means we can utilize all the space.

O(n) time for 3 passes over the height array.
O(n) space to store the max_left and max_right arrays
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = []
        max_right = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
            else:
                max_left.append(max(max_left[i-1], height[i-1]))
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                max_right[i] = 0
            else:
                max_right[i] = max(max_right[i+1], height[i+1])
        
        # amount of water on each idx will be the min of both sides - height of that idx
        res = 0
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                res += water
        
        return res
