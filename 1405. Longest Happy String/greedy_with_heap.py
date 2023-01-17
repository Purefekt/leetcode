"""
Greedy with heap
Use the character with the highest remaining frequency as the next letter, BUT if the previous 2 chars are the same as it,
then block it and add the next highest freq char to the result. Then re add the blocked char to the heap

O(nlogn) time to go through all the chars and pop from heap, where n is the sum of a,b and c
O(n) space to store in heap
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        pq = []
        if a>0: pq.append((-a,'a'))
        if b>0: pq.append((-b,'b'))
        if c>0: pq.append((-c,'c'))

        heapq.heapify(pq)

        print(pq)

        res = ''
        while pq:
            
            frequency, next_char = heapq.heappop(pq)

            # if the third char is repeating
            if len(res)>1 and res[-1] == res[-2] and res[-2] == next_char:
                block_frequency, block_char = frequency, next_char

                if not pq:
                    break
    
                frequency, next_char = heapq.heappop(pq)
                res += next_char
                frequency += 1

                # add this back to the heap with 1 less frequency
                if frequency < 0:
                    heapq.heappush(pq, (frequency, next_char))
                # add the blocked char back to the heap
                heapq.heappush(pq, (block_frequency, block_char))
            else:
                res += next_char
                frequency += 1

                if frequency < 0:
                    heapq.heappush(pq, (frequency, next_char))
        
        return res
