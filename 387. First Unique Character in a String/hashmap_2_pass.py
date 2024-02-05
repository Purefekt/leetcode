class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = collections.defaultdict(int)

        for c in s:
            freq[c] += 1
        
        once = set()
        for k,v in freq.items():
            if v == 1:
                once.add(k)
        
        if len(once) == 0:
            return -1
        
        for i,c in enumerate(s):
            if c in once:
                return i