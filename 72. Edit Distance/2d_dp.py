"""
2d DP.
Create a dp matrix of size m*n, where m = len(word1)+1 and n = len(word2)+1.
dp[0][0] means the edit distance where word1 = "" and word2 = "", which is 0.
dp[0][1] means the edit distance where word2 is of size 1 and word1 = "", this means it will be 1 due to 1 deletion.
Thus pre fill the first row and first column with increasing numbers 1,2,3...
Start filling from (1,1) till (m-1,n-1).
If both characters are the same, no operating is done, take the value from the diagnal.
If they are different, get the min of left, top and diagnol and add 1.
Result will be at dp[-1][-1].

O(m*n) time where m and n are lengths of word1 and word2.
O(m*n) space for the table.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1) + 1
        n = len(word2) + 1

        dp = []
        for i in range(m):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)
        
        for j in range(n):
            dp[0][j] = j
        for i in range(m):
            dp[i][0] = i
        dp[0][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[-1][-1]
        