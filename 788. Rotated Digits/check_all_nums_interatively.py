"""
Check each num by converting it to a string and checking if the flip is different from original.

O(n) time which takes O(n*5) time since we run the find_reverse on each string which can be at max 5 digits.
O(1) space.
"""

class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        mapping = {
            '0':'0',
            '1':'1',
            '2':'5',
            '5':'2',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        res = 0

        def find_reverse(num):
            new_num = ''
            for c in num:
                if c not in mapping:
                    return -1
                new_num += mapping[c]
            return int(new_num)
                

        for i in range(1, n+1):
            num = str(i)
            rev = find_reverse(num)
            if rev == -1 or rev == i:
                continue
            else:
                res += 1
        
        return res
        