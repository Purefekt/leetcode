class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq = collections.defaultdict(int)
        for n in arr:
            freq[n] += 1
        
        values = set()
        for v in freq.values():
            if v in values:
                return False
            else:
                values.add(v)

        return True
        