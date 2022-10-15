class Solution:
    def myAtoi(self, s: str) -> int:
        
        # ignore whitespace
        s = s.lstrip()
        
        # if len s is 0
        if len(s) < 1:
            return 0
        
        # if first element is not a number or + or -, then return 0
        valid = set(['0','1','2','3','4','5','6','7','8','9','+','-'])
        nums = set(['0','1','2','3','4','5','6','7','8','9'])
        if s[0] not in valid:
            return 0
        if s[0] == '+' or s[0] in nums:
            sign_flag = 1
        else:
            sign_flag = -1
        
        # if the first element is - or + then remove it
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        
        # build the res string for only nums. stop if the next element is not a num
        res = ''
        for n in s:
            if n not in nums:
                break
            res += n
        
        # if len of res string is 0 then we dont have a valid num, return 0
        if len(res) < 1:
            return 0
        # if res has a len of >0 then convert that to int and multiply with the sign_flag
        res = int(res)
        res *= sign_flag
        
        
        # clip the int in the given range
        if res < -2**31:
            return -2**31
        if res > 2**31 -1:
            return 2**31 -1
        return res
        