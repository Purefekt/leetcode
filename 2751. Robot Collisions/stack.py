"""
Annoying stack problem.
First sort the healths and directions by the positions.
Before doing this, track the index they appeared in ie give 0 index to the robot who is i=0 in the input. Since output needs to be in THIS order.
Create a stack. If current robot dir is R, simply add to stack.
If current robot dir is L and stack is empty, simply add to stack.
If current robot is L and top of stack is R, we need to remove the top robot and compare.
If the robot at the top of stack is removed, continue to remove.
If the current robot is smaller than the one at the top of stack, then we stop.
If both are the same, none is added and we also stop.
Return the output by sorting the stack with the indexes initially stored.

O(nlogn) time for 2 sort operations and linear pass over the input for all stack operations.
O(n) space used for sorting and stack.
"""

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        pos_healths = []
        for i in range(len(positions)):
            pos_healths.append([positions[i], healths[i], directions[i], i])
        pos_healths.sort()
        
        positions = [p for p,h,d,i in pos_healths]
        healths = [h for p,h,d,i in pos_healths]
        directions = [d for p,h,d,i in pos_healths]
        idx = [i for p,h,d,i in pos_healths]

        stack = []
        for i in range(len(positions)):
            if directions[i] == 'R':
                stack.append((healths[i], directions[i], idx[i]))
            else:
                if stack:
                    flag = True
                    cur_health = healths[i]
                    cur_dir = directions[i]
                    cur_pos = idx[i]
                    while stack and stack[-1][1] == 'R' and cur_dir == 'L':
                        prev, prev_dir, pos = stack.pop()
                        if prev == cur_health:
                            flag = False
                            break
                        else:
                            cur_health = max(prev, cur_health)-1
                            cur_dir = 'R' if prev > cur_health else 'L'
                            cur_pos = pos if prev > cur_health else cur_pos
                    if flag:
                        stack.append((cur_health, cur_dir, cur_pos))
                else:
                    stack.append((healths[i], directions[i], idx[i]))
        
        stack.sort(key=lambda x:x[2])
        res = [a for a,b,c in stack]
        return res
