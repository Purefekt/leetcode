class Solution:
    def numSquares(self, n: int) -> int:

        if n==1:
            return 1
        
        # get all perfect squares < n
        options = []
        for i in range(1,n):
            if i**2 <= n:
                options.append(i**2)
            else:
                break
        
        memo = {}
        def backtrack(val):
            if val in memo:
                return memo[val]

            if val == n:
                memo[val] = 0
                return 0
            
            if val > n:
                memo[val] = math.inf
                return math.inf
            
            res = math.inf
            for i in range(len(options)):
                res = min(res, backtrack(val+options[i]) + 1)
            
            memo[val] = res
            return res
        
        return backtrack(0)
