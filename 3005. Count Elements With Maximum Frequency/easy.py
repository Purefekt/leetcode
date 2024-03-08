class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        max_f = max(freq.values())
        res = 0
        for k,v in freq.items():
            if v == max_f:
                res += max_f
        
        return res
        