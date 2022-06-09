class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
                
        if numRows == 1:
            return [[1]]
        
        # initialize first two rows
        output = [[1], [1,1]]
        
        # populate the next rows
        next_row = []
        for i in range(2,numRows):
            # initialize the next row with 1 on ends of each
            next_row = [0]*(i+1)
            next_row[0], next_row[-1] = 1, 1
            
            # populate the remaining elements of each row
            prev_row = output[i-1]
            for j in range(1, i):
                next_row[j] = prev_row[j-1] + prev_row[j]
            
            # add next row to output
            output.append(next_row)
        
        return output