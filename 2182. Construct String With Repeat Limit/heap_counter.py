"""
Maxheap with counter.
Get a counter of all chars.
Create a maxheap with (-ord val, char, count).
-ord val will help us maintain the maxheap.
Now pop the top element, if this was the one previously used, then we need to keep it aside on cooldown.
During cooldown, we pop the next char and add it just once. To maintain lexicographically largest string.
Then we put it back to the heap (given its count is still >0) and also add the cooldown char.
In the case where the top element is valid, simply add it to the string at max repeatLimit times.

O(nlogn) time. creating pq takes n time and while loop runs n time with heap operations within it taking logn time.
O(n) space used by heap and counter map.
"""

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        # get freq
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        
        # add it to a maxheap
        pq = []
        for c,count in counter.items():
            pq.append((-ord(c), c, count))
        heapq.heapify(pq)

        res = []
        while pq:
            ord_val, c, count = heapq.heappop(pq)
            # if prev char was the same as this, then we skip it
            if res and res[-1][0] == c:
                if not pq:
                    break
                next_ord_val, next_c, next_count = heapq.heappop(pq)
                res.append(next_c)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(pq, (next_ord_val, next_c, next_count))
                heapq.heappush(pq, (ord_val, c, count))
            else:
                res.append(c*min(repeatLimit, count))
                count -= repeatLimit
                if count > 0:
                    heapq.heappush(pq, (ord_val, c, count))
        
        return ''.join(res)
