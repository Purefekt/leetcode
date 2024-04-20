class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        hashmap = {}

        for i, score in items:
            if i not in hashmap:
                hashmap[i] = []
                heapq.heapify(hashmap[i])
            
            heapq.heappush(hashmap[i], -score)
        
        res = []
        for i in hashmap:
            total = 0
            for _ in range(5):
                total += heapq.heappop(hashmap[i])
            res.append((i, (-total)//5))
        
        res.sort()
        return res
