"""
Top down 2d dp.
We can have a recursive function which takes index and subsequence length.
Index here is the current index of 's' which we are checking to either keep or skip.
Subsequence length is the size of current subsequence which is formed by all the 'keep' moves in the decision tree.
We either keep or skip the current s[idx].
We can keep only if s[idx] == t[subseq_len] since they must be the same character. Also check if subseq_len < len(t).
Base case if idx == len(s), we check if the subsequence length is len(t), this verifies that we have found a valid subsequence which is t.
Memoiz on (idx, subseq_len).

O(m*n) time where size of s is m and size of t is n.
O(m*n) space to store the memo table.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}
        def helper(idx, subseq_len):
            if (idx, subseq_len) in memo:
                return memo[(idx, subseq_len)]

            if idx == len(s):
                if subseq_len == len(t):
                    memo[(idx, subseq_len)] = 1
                    return 1
                else:
                    memo[(idx, subseq_len)] = 0
                    return 0
            
            res = 0
            # keep, only if valid
            if subseq_len < len(t):
                if s[idx] == t[subseq_len]:
                    res += helper(idx+1, subseq_len+1)

            # skip
            res += helper(idx+1, subseq_len)

            memo[(idx, subseq_len)] = res
            return res
        
        return helper(0, 0)
