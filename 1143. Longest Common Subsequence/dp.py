"""
Dynamic Programming
Create a 2d matrix of m*n where m is len(text1)+1 and n is len(text2)+1
the last row and last col will be all 0s since for dp[m-2][n-1] (2nd last row and last column) we are trying to find the LCS between text1 and a string of 0 elements so it is 0
We start filling from dp[m-2][n-1] right to left, bottom to top
If for any cell, the 2 characters are equal, the value in that cell will be 1 + value in the cell to its bottom right diagnol cell
Else if the 2 characters are not equal, then the value in that cell will be max(value below, value to right)
Solution will be at dp[0][0]

O(m*n) time
O(m*n) space
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = []
        for i in range(len(text1)+1):
            dp_row = []
            for j in range(len(text2)+1):
                dp_row.append(0)
            dp.append(dp_row)
        
        for row in dp:
            print(row)
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
