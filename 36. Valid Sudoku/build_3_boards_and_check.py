class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use hashmaps to check for each row, column and 3x3 sub box
        
        # rows
        rows_validity = self.validity(board = board)
        if rows_validity == False:
            return False
        
        # columns
        # build a board with 9 columns as the rows
        curr_col = []
        cols_board = []
        for i in range(0,9):
            for j in range(0,9):
                if len(curr_col) < 10:
                    curr_col.append(board[j][i])
                if len(curr_col) == 9:
                    cols_board.append(curr_col)
                    curr_col = []
        
        cols_validity = self.validity(board=cols_board)
        if cols_validity == False:
            return False
        
        # 3x3 sub box
        # build a board with 9 sub boxes as the rows
        top_left = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        curr_sub_box = []
        sub_box_board = []
        for i in range(len(top_left)):
            start_r = top_left[i][0]
            start_c = top_left[i][1]
            
            for j in range(start_r, start_r+3):
                for k in range(start_c, start_c+3):
                    curr_sub_box.append(board[j][k])
            
            sub_box_board.append(curr_sub_box)
            curr_sub_box = []
        
        sub_box_validity = self.validity(board=sub_box_board)
        if sub_box_validity == False:
            return False
    
        # return True is passed all 3 cases
        return True
 
    # this func takes in a board and returns if its valid or not    
    def validity(self, board):
        for row in board:
            hashmap_count = {}
            for num in row:
                if num != '.':
                    if num in hashmap_count.keys():
                        return False
                    else:
                        hashmap_count[num] = 1
                    
        return True
        