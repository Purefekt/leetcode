"""
Linear solution O(N) using bucketsort.

initialize a frequency array of size len(nums)+1. 
Each index corresponds to a frequency. get the frequencies of each num in a hashmap and then populate the frequency array with nums based on their frequency.

for example is nums = [1,1,1,2,2,3]
frequency (initially) = [None, None, None, None, None, None, None]
frequency (after populating) = [None, [3], [2], [1], None, None, None]
index pos 0 will always be None. We use lists since if 2 nums have the same freq then they will be added as [x,y]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initialize an array of len => len(nums)+1
        frequency = [None]*(len(nums)+1)
        # create hashmap of counts of each num
        count_map = collections.Counter(nums)
        
        # populate the frequency array
        for key, val in count_map.items():
            if not frequency[val]:
                frequency[val] = [key]
            elif frequency[val]:
                frequency[val].append(key)
        
        # now add the elements to output from the right end
        output = []
        while len(output) < k:
            for i in range(len(frequency)-1,-1,-1):
                if frequency[i]:
                    output.extend(frequency[i])
        
        return output[:k]
    