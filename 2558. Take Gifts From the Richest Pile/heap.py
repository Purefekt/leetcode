class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = [-c for c in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            if gifts:
                richest = heapq.heappop(gifts)
                richest *= -1
                leave = math.floor(math.sqrt(richest))
                heapq.heappush(gifts, -leave)
        
        return -sum(gifts)
