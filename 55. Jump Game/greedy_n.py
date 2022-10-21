"""
GREEDY
Set the last index as goal and move the goal backwards. To move the goal, check the prev element.
If the prev elements index and maxjump >= the goal_index, this means this cell can reach the goal. update goal_index to this cell since if we reach this then we are gauranteed to reach the goal.
At the end of the pass, if the goal_index is 0, this means first element can reach the goal

O(n) time since we do one pass over the array
O(1) space since we store the goal_index in constant space.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal_index = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i
        
        if goal_index == 0:
            return True
        return False
    