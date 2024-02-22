class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # get frequencies of each number and their first and last indexes
        freq = collections.defaultdict(int)
        first_index = {}
        last_index = {}
        for i,n in enumerate(nums):
            freq[n] += 1
            if n not in first_index:
                first_index[n] = i
            last_index[n] = i
        
        max_freq = max(freq.values())
        candidates = []
        for k,v in freq.items():
            if v == max_freq:
                candidates.append(k)
        
        res = len(nums)
        for c in candidates:
            res = min(res, (last_index[c]+1)-first_index[c])
        
        return res
