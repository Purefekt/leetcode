"""
Brute force solution. BAD
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a counter for each number
        counter_map = collections.Counter(nums)
        
        output = []
        max_k = 0
        for i in range(k):
            # find current max_k
            for v in counter_map.values():
                max_k = max(max_k, v)
            
            for k,v in counter_map.items():
                if v == max_k:
                    output.append(k)
                    counter_map[k] = 0
                    max_k = 0
                    break
        
        return output
            