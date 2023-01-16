"""
Build a hashmap of cell position and their next cell. To do this start from the last row and move upwards
First go left to right and then decrement the row (move up) and go right to left. To simulate how one would move in a snakes and ladders game
For a 6x6 board, our hashmap will have keys from 1-36. If a position has a ladder or a snake, its value will be the end value otherwise its value will be itself
Run BFS from position 1 and explore the graph, we can move from position+1 till position+6 (in bounds)
Count the number of levels, that is the number of moves, if at any point we hit n*n position, return the number of moves

O(n^2) time. One pass to build the hashmap and one pass for bfs. Since we use visited, we only visit each cell once
O(n^2) space to store the values in the hashmap
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        # create a hashmap of positions and next positions
        hashmap = {}
        idx = 1
        i = n-1
        while i>=0:
            for j in range(n):
                if board[i][j] == -1:
                        hashmap[idx] = idx
                else:
                    hashmap[idx] = board[i][j]
                idx += 1
            i -= 1
            if i<0:
                break
            for j in range(n-1, -1, -1):
                if board[i][j] == -1:
                        hashmap[idx] = idx
                else:
                    hashmap[idx] = board[i][j]
                idx += 1
            i -= 1
        
        
        count = 0
        queue = [1]
        visited = set([1])
        while queue:
            count += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for i in range(1,7):
                    if node+i in hashmap:
                        if hashmap[node+i] == n*n:
                            return count
                        if hashmap[node+i] not in visited:
                            queue.append(hashmap[node+i])
                            visited.add(hashmap[node+i])
        
        return -1
        