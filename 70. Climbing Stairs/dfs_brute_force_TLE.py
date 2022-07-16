"""
Simple DFS. Leads to TLE. Runs in exponential time.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = 0
        
        stack = collections.deque()
        stack.append(0)
        
        while stack:
            node = stack.pop()
            if node == n:
                result += 1
            elif node > n:
                continue
            else:
                stack.append(node+2)
                stack.append(node+1)
        
        return result
    