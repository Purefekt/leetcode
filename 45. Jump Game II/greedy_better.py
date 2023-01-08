"""
Greedy solution
Start from the first index, for this see the furthest it can go to, 
next take all the cells reachable by the previous cell and find the farthest we can go from this group of cells
For example for the input [2,3,1,1,2,2], the levels are [[2],[3,1],[1,2],[2]] and this takes 3 jumps. Thus we increase count when moving from one level to the next
Code this using l and r pointers, and stop when r surpasses len(nums)-1

O(n) time to go over all cells once
O(1) space
"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        l = 0
        r = 0

        count = 0
        while r<len(nums)-1:
            count += 1

            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
        
        return count
        