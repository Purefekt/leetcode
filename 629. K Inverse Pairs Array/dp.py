class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # Initialize a 2D array to store the results
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Base case: when n is 0, there's only one permutation with 0 inverse pairs
        dp[0][0] = 1

        # Fill in the DP table
        for i in range(1, n + 1):
            dp[i][0] = 1  # Number of permutations with 0 inverse pairs is always 1
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % (10**9 + 7)
                if j >= i:
                    dp[i][j] = (dp[i][j] % (10**9 + 7) - dp[i - 1][j - i] ) % (10**9 + 7)

        return dp[n][k] % (10**9 + 7)
        