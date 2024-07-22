class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        combined = []
        for i in range(len(names)):
            combined.append((heights[i], names[i]))
        combined.sort(reverse=True)

        res = [b for a,b in combined]

        return res
