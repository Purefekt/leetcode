"""
Dynamic Programming. Create a dp matrix of m*n. m is the number of rows = len(coins)+1 and n is the number of columns = amount+1
The first col is when amount is 0, second column is when the amount is 1 and so on
The first row is when using no coins, the second row is when using only the smallest denomination of coins, the third row is when using the 2 smallest denominations and so on
For this we need to sort coins in non decreasing order
Initialize the first row, dp[0][0] will be 1, this is when we have 0 coins to make an amount 0, we have 1 way to do this. All other cells in first row will be 0 since we have 0 ways to make amount 1,2,etc with no coins
We start to fill the dp matrix from dp[1,0] till dp[-1][-1] left to right top to bottom.
For the 2nd row, we assume we have denominations of the smallest coin, we the value till amount=coin-1 will be the value from the cell above it. For the remaining it will be the sume of the value above it and the value to the left of it -coin value
Solution will be at dp[-1][-1]

O(n*m) where n is the number of distinct coins and m is the max amount
O(n*m) space to store the dp matrix
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # create a dp matrix of m*n. m is the number of rows == number of distinct coins + 1, n is amount+1
        dp = []
        for i in range(len(coins)+1):
            dp_row = []
            for j in range(amount+1):
                dp_row.append(0)
            dp.append(dp_row)
        
        # when there are no coins and 0 amount, we have 1 way to make up the amount 0
        dp[0][0] = 1

        # start filling the dp matrix from the smallest coins denomination
        coins.sort()

        # for each coin, fill all the values till the value of that coin. For coin 5, we fill till amount 4. The value is the one above it
        for i in range(1,len(coins)+1):
            coin = coins[i-1]
            for j in range(len(dp[0])):
                
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coin]
        
        return dp[-1][-1]
