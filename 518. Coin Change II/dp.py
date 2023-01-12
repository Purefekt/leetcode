"""
Dynamic Programming. Build a 2D matrix of m*n. 
A row for each value of denomination + 0, thus m = len(coins)+1
A col for each value from 0 till amount, thus n = amount + 1
dp[0][0] means how many ways to make amount 0 with coins = [0], that is 1 way. the remaining dp[0] row is how many ways to make amounts 1..amount, using coins = [0], which is 0 ways
Sort the coins array to build the solution using smaller coins first and then larger
fill the dp matrix from dp[1][0] -> dp[m-1][n-1]
for each row, copy the values from the row above till amount < coin denomination value. Since these will not change even with the addition of a coin since this coin is itself larger than the amount
for the other cells, dp[i][j] = dp[i][j-coin]+dp[i-1][j]

O(n*m) where n is the number of distinct coins and m is the max amount
O(n*m) space to store the dp matrix
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()

        m = len(coins)+1
        n = amount+1

        # build dp matrix
        dp = []
        for i in range(m):
            dp_row = []
            for j in range(n):
                dp_row.append(0)
            dp.append(dp_row)

        # initialize dp matrix
        dp[0][0] = 1

        for i in range(1,m):
            coin = coins[i-1]
            for j in range(n):
                if j<coin:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coin]
        
        return dp[-1][-1]
