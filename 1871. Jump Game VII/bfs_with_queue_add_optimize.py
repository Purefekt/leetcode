"""
BFS but built the queue with least amount of space used.
Run BFS with 0 as the first node in queue.
Children of a node will be all indexes in range [node+minJump, min(node+maxJump, len(s)-1)].
Only add children to queue is s[child] == '0'.
Do not add children which are already in the queue, do this by using a variable Farthest.
This variable = node + maxjump at the end of a nodes search, so when we search the next node, do not add any nodes which are less than or equal to it.
Thus the range of children for a node will be [max(node+minJump, farthest+1), min(node+maxJump, len(s)-1)].
Return True if farthest == len(s)-1, else False.

O(n) time to visit each node at most once.
O(n) space to store at most n elements in queue
""" 

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[-1] == '1':
            return False

        queue = [0]
        farthest = 0

        while queue:
            node = queue.pop(0)

            min_j = max(node + minJump, farthest+1)
            max_j = min(node + maxJump, len(s)-1)
            for i in range(min_j, max_j+1):
                if s[i] == '0':
                    queue.append(i)
                    # return if we already reached the end
                    if i == len(s)-1:
                        return True
            farthest = node + maxJump
        
        print(farthest)
        if farthest == len(s)-1:
            return True
        return False
        