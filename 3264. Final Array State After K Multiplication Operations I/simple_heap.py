class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        pq = []
        for i,n in enumerate(nums):
            pq.append((n,i))
        heapq.heapify(pq)
        
        for _ in range(k):
            num, idx = heapq.heappop(pq)
            num *= multiplier
            heapq.heappush(pq, (num, idx))
        
        # sort across 2nd index which are the indexes
        pq.sort(key=lambda x:x[1])

        res = [n for n,i in pq]
        return res
        