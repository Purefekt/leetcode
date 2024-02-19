"""
Get frequency of each digit from 0-9 in the number.
If the number was positive, get the smallest number which is NOT 0 and set it to the first number in the result.
Then add all 0s, then add the remaining numbers in increasing order.
If the number was negative, build the result in reverse order.

O(n) time.
O(1) space since the hashmap is of constant size.
"""

class Solution:
    def smallestNumber(self, num: int) -> int:

        if num == 0:
            return 0
        
        positive = True
        if num < 0:
            positive = False
        
        num = str(num)
        if positive is False:
            num = num[1:]
        
        # get frequency of each number
        freq = collections.defaultdict(int)
        for n in num:
            freq[int(n)] += 1
        
        zero_freq = 0
        if 0 in freq:
            zero_freq = freq[0]
            del freq[0]
        
        res = ''

        if positive is True:
            # if positive, get the smallest number and set it as first
            smallest = min(freq.keys())
            freq[smallest] -= 1
            res += str(smallest)
            # then add all occurances of 0
            res += str(0) * zero_freq
            # now add the others in increasing order
            for n in sorted(freq.keys()):
                res += str(n) * freq[n]
            res = int(res)
        
        else:
            # if negative, build the number using the largest to 0
            for n in sorted(freq.keys(), reverse=True):
                res += str(n) * freq[n]
            res += str(0) * zero_freq
            res = -int(res)

        return res
