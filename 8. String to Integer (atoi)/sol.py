"""
Strip
check for negative flag and remove - or + sign
iterate through the string and keep adding only numbers, at anything else break
if the len of answer is < 1, means no numbers were found, return 0
add neg flag is required
check for clipping
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        
        # edge cases
        if len(s) < 1:
            return 0
        
        # check for negative flag
        neg_flag = 0
        if s[0] == '-':
            neg_flag = 1
            # remove negative sign from the string
            s = s[1:]
        elif s[0] == '+':
            # remove positive sign from the string
            s = s[1:]
        else:
            pass
        
        ans = ''
        for i in range(len(s)):
            if ord(s[i])<ord('0') or ord(s[i])>ord('9'):
                break
            else:
                ans += s[i]
        
        if len(ans) < 1:
            return 0
        
        # add neg if exists
        if neg_flag == 1:
            ans = '-' + ans
        
        # checks for clipping
        ans = int(ans)
        if ans > math.pow(2,31)-1:
            return int(math.pow(2,31))-1
        elif ans < -math.pow(2,31):
            return int(-math.pow(2,31))
        else:
            return ans
        