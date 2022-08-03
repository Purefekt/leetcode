"""
Using min heap with -negative counters. Since we need the largest frequent nums, convert all frequencies to negative so that min heap gives the smallest (actually largest) element.

O(Nlogk) solution
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create counter for freq of nums
        counter_map = collections.Counter(nums)
        # create an array where each element is a tuple (-frequency, num).
        counter_list = []
        for key,val in counter_map.items():
            counter_list.append((-val,key))

        # use priority queue to get the smallest freq (largest since negative)
        heapq.heapify(counter_list)
        output = []
        for i in range(k):
            freq, num = heapq.heappop(counter_list)
            output.append(num)
        
        return output
    