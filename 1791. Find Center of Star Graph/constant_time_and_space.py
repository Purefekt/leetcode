class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        first = edges[0]
        second = edges[1]

        count = collections.defaultdict(int)
        count[first[0]] += 1
        count[first[1]] += 1
        count[second[0]] += 1
        count[second[1]] += 1

        max_val = max(count.values())
        for k,v in count.items():
            if v == max_val:
                return k