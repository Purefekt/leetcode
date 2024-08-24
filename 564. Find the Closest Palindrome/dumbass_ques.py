"""
Stupid problem, should not be asked in interviews.
There are 5 candidates for closest palindromic number.
option1: Mirror the first half (left side) of numbers, since this will be closer than mirroring second half (right side).
option2: Increment first half by 1 and mirror that.
option3: Decrement first half by 1 and mirror that.
option4: closest all 9 number of size 1 less than size of n. So for 1234, it will be 999.
option5: closest number of the form 10..01 of size 1 more than n. So for 1234, it will be 1001.
Compare the distances of these 5 options and return the closest.

O(n) time.
O(n) space.
"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        if len(n) == 1:
            return str(int(n)-1)

        candidates = []

        # get first half, there will be an extra single char if size of n is odd
        mid = len(n)//2
        first_half = n[:mid]
        extra = n[mid] if len(n) % 2 == 1 else ''

        # mirror the first half
        option = first_half
        if extra:
            option += extra
        for i in range(len(first_half)-1, -1, -1):
            option += first_half[i]
        if option != n:
            candidates.append(option)

        # drecrement first half and mirror it
        if extra:
            extra = int(extra)
            extra -= 1
            extra = str(extra)
        else:
            first_half = int(first_half)
            first_half -= 1
            first_half = str(first_half)
        option = first_half
        if extra:
            option += extra
        for i in range(len(first_half)-1, -1, -1):
            option += first_half[i]
        if extra and int(extra) >= 0:
            candidates.append(option)
        elif not extra:
            candidates.append(option)
        
        # increment first half and mirror it
        if extra:
            extra = int(extra)
            extra += 2 # to correct for previous decrement of 1
            extra = str(extra)
        else:
            first_half = int(first_half)
            first_half += 2 # to correct for previous decrement of 1
            first_half = str(first_half)
        option = first_half
        if extra:
            option += extra
        for i in range(len(first_half)-1, -1, -1):
            option += first_half[i]
        candidates.append(option)

        # closest 99...99 which is lower than num of digits of n
        option = '9' * (len(n)-1)
        candidates.append(option)

        # closest 10..01 which is higher than num of digits of n
        option = '1'
        option += '0' * (len(n)-1)
        option += '1'
        candidates.append(option)

        # compare all options and return best
        min_dis = math.inf
        res = None
        for c in candidates:
            if abs(int(c) - int(n)) < min_dis:
                res = c
                min_dis = abs(int(c) - int(n))
            elif abs(int(c) - int(n)) == min_dis:
                if int(c) < int(res):
                    res = c
        
        return res
