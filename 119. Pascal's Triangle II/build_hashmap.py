"""
Build a hashmap with key as level number and value as the level. 
Initialize each level with len level number + 1 and set first and last element to 1. Then use previous level to build it till rowIndex.
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        level_vals = {
            0 : [1],
            1 : [1,1]
        }
        
        if rowIndex < 2:
            return level_vals[rowIndex]
        
        # build the hashmap
        for i in range(2,rowIndex+1):
            # initialize and set first and last element to 1
            current_level = [0]*(i+1)
            current_level[0], current_level[-1] = 1,1
            
            # loop over and fill the remaining vals
            for j in range(1,len(current_level)-1):
                prev_level = level_vals[i-1]
                current_level[j] = prev_level[j-1] + prev_level[j]
            
            # add this level to the hashmap
            level_vals[i] = current_level
        
        return level_vals[rowIndex]
                