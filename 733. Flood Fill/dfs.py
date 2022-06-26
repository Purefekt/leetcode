class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # no change if that pixel is already of the given color
        if image[sr][sc] == color:
            return image
        
        # get num of rows and cols
        rows = len(image)
        cols = len(image[0])
        
        original_col = image[sr][sc]
        
        stack = collections.deque()
        stack.append((sr,sc))
        
        while stack:
            i,j = stack.pop()
            
            # change color
            image[i][j] = color
            
            # add 4 directional pixels IF they are valid:
            # up (-1,0)
            if i-1>=0 and j>=0 and i-1<rows and j<cols and image[i-1][j]==original_col:
                stack.append((i-1,j))
            # right (0,1)
            if i>=0 and j+1>=0 and i<rows and j+1<cols and image[i][j+1]==original_col:
                stack.append((i,j+1))
            # down (1,0)
            if i+1>=0 and j>=0 and i+1<rows and j<cols and image[i+1][j]==original_col:
                stack.append((i+1,j))
            # left (0,-1)
            if i>=0 and j-1>=0 and i<rows and j-1<cols and image[i][j-1]==original_col:
                stack.append((i,j-1))
        
        return image
    