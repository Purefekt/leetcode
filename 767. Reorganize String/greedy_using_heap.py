"""
Get the frequencies of all characters and put them in a max heap
simulate a max heap using a min heap by negating the frequencies
Build the result one by one, take out the most frequent character and append it to the result
BUT if the most frequent character is the same as the previous one, we need to take the next most frequent, thus put a HOLD on the previous most frequent
Following this logic, our result will not have the same number of characters as the original string if a combination is not possible

O(nlogn) time using heap
O(n) space for heap
"""

class Solution:
    def reorganizeString(self, s: str) -> str:

        freqs_map = {}
        for c in s:
            if c not in freqs_map:
                freqs_map[c] = 1
            else:
                freqs_map[c] += 1
        
        pq = []
        for k,v in freqs_map.items():
            pq.append([-v,k])
        
        res = ''
        prev = None
        heapq.heapify(pq)
        
        while pq:
            cache = heapq.heappop(pq)
            freq, c = cache

            if c == prev:
                if pq:
                    freq, c = heapq.heappop(pq)
                    res += c
                    freq += 1
                    prev = c
                    if freq < 0:
                        heapq.heappush(pq, [freq,c])
                    heapq.heappush(pq, cache)
            
            else:
                res += c
                freq += 1
                prev = c
                if freq < 0:
                    heapq.heappush(pq, [freq,c])
        
        if len(res) == len(s):
            return res
        return ""
            