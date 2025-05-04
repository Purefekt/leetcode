class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # get the original color
        # start bfs from (sr, sc)
        # add new cells if they are the new color
        # update input image so we do not need visited

        m,n = len(image), len(image[0])
        original_color = image[sr][sc]

        # edge case if original color and color are the same
        if original_color == color:
            return image

        queue = collections.deque()
        queue.append((sr,sc))
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            node = queue.popleft()
            i,j = node
            image[i][j] = color
            for d in directions:
                dest = tuple(map(lambda x,y: x+y, node, d))
                r,c = dest
                if 0<=r<m and 0<=c<n and image[r][c] == original_color:
                    queue.append(dest)
        
        return image
