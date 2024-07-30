"""
Dp recursion with memoization.
We need to find the largest valid string we can make.
Result will be len(s) - larges string.
Helper function takes index and prev char. Char is used to determine the next char.
At each step we can either skip the current char or add it. If we add it, we add 1 to the length.
To add a char, if the prev char is 'a', simply add it.
If the prev char is 'b', only add if current char is 'b'.
Instead of a simply hashmap storing (index, char) pair, use a 2d array to store the memo values.
This is because storing (index, char) will give memory limit since index can go to 10^5.
Using a 2*n array will allow to skip storing the actual index.

O(n) time since we make at max 2*n calls.
O(n) space since the stack and memo table uses 2*n space.
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        memo = []
        for i in range(2):
            row = []
            for j in range(len(s)+1):
                row.append(None)
            memo.append(row)

        def helper(idx, char):
            char_idx = 0 if char == 'a' else 1
            if memo[char_idx][idx]:
                return memo[char_idx][idx]
            if idx == len(s):
                return 0
            
            # skip current char
            skip = helper(idx+1, char)

            # keep only if next is b or if current is a 
            keep = 0
            if char == 'a':
                keep += 1 + helper(idx+1, s[idx])
            else:
                if s[idx] == 'b':
                    keep += 1 + helper(idx+1, s[idx])

            memo[char_idx][idx] = max(skip, keep)
            return max(skip, keep)
        
        return len(s) - helper(0, 'a')
