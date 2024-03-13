class Solution:
    def pivotInteger(self, n: int) -> int:
        
        lsum = 0
        rsum = 0
        l = 1
        r = n
        while l<r:
            if lsum < rsum:
                lsum += l
                l += 1
            elif rsum < lsum:
                rsum += r
                r -= 1
            else:
                lsum += l
                l += 1
        
        if lsum == rsum:
            return l
        else:
            return -1
        