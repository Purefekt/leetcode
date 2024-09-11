class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        start = bin(start)
        start = start[2:]
        
        goal = bin(goal)
        goal = goal[2:]

        if len(start) > len(goal):
            prefix = "0" * (len(start)- len(goal))
            goal = prefix + goal
        elif len(goal) > len(start):
            prefix = "0" * (len(goal) - len(start))
            start = prefix + start
        
        res = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                res += 1
        
        return res
