"""
Use bfs level order and keep track of the moves (depth). Return moves when hit the target.
For each node, per each move there will be 8 children. 
For [0,0,0,0] => [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1], [9,0,0,0], [0,9,0,0], [0,0,9,0], [0,0,0,9]
Keep visited to not go back to prev nodes

O(10000) since we can visit all 10000 possibilites once
O(10000) space since we can store in the worst case all possibilities in visited set
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def get_children(node_string):
            node_list = [c for c in node_string]
            children_list = []

            for i in range(4):
                num = int(node_list[i])
                num_up = (num+1)%10
                num_down = (num-1+10)%10
                
                up = node_list[:]
                down = node_list[:]
                up[i] = str(num_up)
                down[i] = str(num_down)

                children_list.append(''.join(up))
                children_list.append(''.join(down))
            
            return children_list
        
        queue = ['0000']
        moves = 0
        visited = set()
        visited.add('0000')
        deadends = set(deadends)

        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)

                if node == target:
                    return moves
                
                if node in deadends:
                    continue

                children_list = get_children(node)
                for child in children_list:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            
            moves += 1
        
        return -1
