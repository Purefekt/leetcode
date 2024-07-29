"""
See editorial
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        res = 0

        inc_dp = []
        for i in range(n):
            row = []
            for j in range(4):
                row.append(0)
            inc_dp.append(row)
        dec_dp = []
        for i in range(n):
            row = []
            for j in range(4):
                row.append(0)
            dec_dp.append(row)
        
        # for each soldier, size of sequence is 1
        for i in range(n):
            inc_dp[i][1] = 1
            dec_dp[i][1] = 1
        
        # dp
        for count in range(2,4):
            for i in range(n):
                for j in range(i+1, n):
                    if rating[j] > rating[i]:
                        inc_dp[j][count] += inc_dp[i][count-1]
                    if rating[j] < rating[i]:
                        dec_dp[j][count] += dec_dp[i][count-1]
        
        for i in range(n):
            res += inc_dp[i][3]
            res += dec_dp[i][3]
        
        return res
