"""
BFS where the entire board is a node.
To get adj nodes, get the index of 0 and try to move it to another position.
Other than this bfs remains the same.
For visited, we need a hashable data structure, we can flatten the board and convert it to a tuple.

O((m*n)! * (m*n)) time since there are (m*n)! different nodes which we traverse through the bfs. To process each node we go through m*n.
O((m*n)!) space used for queue to store all nodes.
"""

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        final_state = (1,2,3,4,5,0)

        def find_zero(state):
            for i in range(2):
                for j in range(3):
                    if state[i][j] == 0:
                        return (i,j)
        
        def get_new_state(state, src, dst):
            new_state = []
            for i in range(2):
                row = []
                for j in range(3):
                    row.append(state[i][j])
                new_state.append(row)
            new_state[src[0]][src[1]], new_state[dst[0]][dst[1]] = new_state[dst[0]][dst[1]], new_state[src[0]][src[1]]
            return new_state
        
        def flat(state):
            res = []
            for i in range(2):
                for j in range(3):
                    res.append(state[i][j])
            return tuple(res)

        queue = [(board,0)]
        visited = set()

        while queue:
            node, depth = queue.pop(0)
            flat_node = flat(node)
            if flat_node == final_state:
                return depth
            if flat_node in visited:
                continue
            
            # find 0th idx
            i,j = find_zero(node)
            # get adj nodes
            if i-1 >= 0:
                new_state = get_new_state(node, (i,j), (i-1, j))
                queue.append((new_state, depth+1))
            if i+1 < 2:
                new_state = get_new_state(node, (i,j), (i+1, j))
                queue.append((new_state, depth+1))
            if j-1 >= 0:
                new_state = get_new_state(node, (i,j), (i, j-1))
                queue.append((new_state, depth+1))
            if j+1 < 3:
                new_state = get_new_state(node, (i,j), (i, j+1))
                queue.append((new_state, depth+1))
            visited.add(flat_node)

        return -1
            