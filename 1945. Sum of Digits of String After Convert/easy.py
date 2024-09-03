class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        # convert
        mid = ""
        for c in s:
            mid += str(ord(c) - ord('a') + 1)
        
        # transform
        for _ in range(k):
            num = 0
            for c in mid:
                num += int(c)
            mid = str(num)
        
        return int(mid)
