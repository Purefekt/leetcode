"""
2d dp top down.
First observation is that repeating char are the same as 1 instance of that char, so aaabbaaba -> ababa. The problem stays the same.
Now we can try different substrings and see if we can do better.
For aba, we can set each char individually and get 3 turns.
Or we can set all to aaa and then flip middle to b, this takes 2 turns.
Helper function takes start and end of a substring.
Set result to 1 + helper(start+1, end) to denote that we are flipping each char individually without any optimization.
Optimization can happen if first and last char of a substring are the same.
Iterate from start+1 till end+1, set this iterator to the new end of substring we want to check. If at any point, s[k] == s[start], we know we can optimize here.
current turns required will be sum of helper(start, k-1) + helper(k+1, end).
Update res to min of res and cur.
Memoiz on this.

O(n^3) time since the helper function runs in n^2 time and for each we iterate from start to end once which takes n time as well.
O(n^2) space used by memoization table. Stack takes up to n space.
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        
        # remove dupes
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                continue
            stack.append(c)
        s = ''.join(stack)

        memo = {}
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            # empty substring
            if start > end:
                return 0
            
            # worst case to print each char separately, thus we need n number of steps
            res = 1 + helper(start+1, end)

            # optimize. If start and end chars of a subarray are same, we can flip them in 1 move and then flip the middle chars. aba -> aaa -> aba
            for k in range(start+1, end+1):
                if s[k] == s[start]:
                    cur = helper(start, k-1) + helper(k+1, end)
                    res = min(res, cur)
            
            memo[(start, end)] = res
            return res
        
        return helper(0, len(s)-1)
