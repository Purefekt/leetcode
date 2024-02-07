"""
Create a hashmap of frequencies of each char.
Convert that hashmap into a list where each element is a tuple (count, char).
Sort this in reversed order.
Build the outside print based on this reversed list.

O(nlogn) time for sort.
O(n) space.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = collections.defaultdict(int)

        for c in s:
            freq[c] += 1
        
        freq_list = []
        for k,v in freq.items():
            freq_list.append((v,k))
        
        freq_list.sort(reverse=True)

        res = ""
        for v,k in freq_list:
            res += k * v
        
        return res
