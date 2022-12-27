"""
Create a HASHMAP of the inner cols frequency. For a brick wall row, the best strategy would be to go through the space between 2 bricks, this is called inner col
For a brick wall of width 6, we have 5 inner cols at positions 1,2,3,4,5
For each row we will increment the frequency of each inner col occurance
To minimize the number of bricks to cut, we need to maxmimize the number of inner cols we go through, so we will take the width-max(inner_col_freq.values) as solution

O(n*k) time. where n is number of rows and k is the number of inner cols. in worst case we have all bricks of size 1 so we have to go through all k bricks
O(k) space to store the freq of all inner cols
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        width = sum(wall[0])
        inner_col_freq = {}

        # go through each row and add to the freq
        for row in wall:
            col = 0
            for brick in row:
                col += brick
                if col not in inner_col_freq:
                    inner_col_freq[col] = 1
                else:
                    inner_col_freq[col] += 1
        
        # delete the last col(right side border)
        del inner_col_freq[width]

        # get the col with max freq
        if len(inner_col_freq) < 1:
            return len(wall)
        col_max_freq = max(inner_col_freq.values())

        return len(wall) - col_max_freq
