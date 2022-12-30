"""
Dynamic Programming. Like coin change problems
Get the largest perfect square which is smaller than n. Then get all perfects squares less than and including the max perfect square. These are like the coins
Set a dp array to len(n)+1. Initialize dp[0] to 0, since we need 0 perfect square numbers to make 0 and set the value of all cells at index perfect square to 1
For example dp[1] = 1 and dp[4] = 1 since we need 1 perfect square to make them
Fill the dp array skipping the ones which are already perfect squares. For an idx, min(dp[idx-ps1], dp[idx-ps2],..)+1. Where psX is a perfect square less than that index
Result will be at dp[-1]

O(n*sqrt(n)) time. O(n) for each number in dp array and for each number we check till less than itself
O(n) space to store dp array
"""
class Solution:
    def numSquares(self, n: int) -> int:
        
        # get all perfect square <= n
        max_ps = 1
        for i in range(n, 0, -1):
            square_root = int(sqrt(i))
            if square_root**2 == i:
                max_ps = square_root
                break
        
        all_ps_set = set()
        all_ps = []
        for i in range(1,max_ps+1):
            all_ps_set.add(i**2)
            all_ps.append(i**2)
        
        # initialize dp array. Set all the cells which are ps to 1 since to get to those we only need 1 ps
        dp = [0 for i in range(n+1)]
        for ps in all_ps:
            dp[ps] = 1
        
        for i in range(1, len(dp)):
            if i not in all_ps_set:
                min_val = inf
                for j in all_ps:
                    if i<j:
                        break
                    min_val = min(dp[i-j], min_val)
                dp[i] = min_val + 1
        
        return dp[-1]
                    