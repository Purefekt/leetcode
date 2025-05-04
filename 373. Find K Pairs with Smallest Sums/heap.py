"""
Heapq.
Actual combinations can be len(nums1) * len(nums2) == 10^10.
Instead of this, we only keep a smaller subset of sequences in the heap.
At first place the following in the pq (sum, n1, n2).
Where n1 is the index of nums1, n2 is the index of nums2 and sum is the sum of numbers at those indexes.
Pop this and place the result [nums1[n1], nums2[n2]] in the result.
Now we can add 2 more items to the heap -> (sum, n1, n2+1) and (sum, n1+1, n2).
Now when we pop from heap. we continue using those indexes, but the heap will always give us the smallest indexes.
Edge case if either of the arrays is completed, thus always check if n+1 < len(nums)
We also need a visited set since there is a chance to add the same indexes again, first check with visited before adding.

O(min(
    k*logk,
    m*n*log(m*n)
)) time since we iterate either k or m*n, whichever is smaller and the heap operation takes another log(value) time.
O(min(k, m*n)) space taken by the heap.
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        pq = [(nums1[0]+nums2[0], 0, 0)]
        heapq.heapify(pq)

        res = []
        visited = set()
        visited.add((0,0))

        while len(res) < k:
            _, n1, n2 = heapq.heappop(pq)
            res.append((nums1[n1], nums2[n2]))

            if n1+1 < len(nums1) and (n1+1, n2) not in visited:
                total = nums1[n1+1] + nums2[n2]
                heapq.heappush(pq, (total, n1+1, n2))
                visited.add((n1+1, n2))
            
            if n2+1 < len(nums2) and (n1, n2+1) not in visited:
                total = nums1[n1] + nums2[n2+1]
                heapq.heappush(pq, (total, n1, n2+1))
                visited.add((n1, n2+1))
        
        return res
