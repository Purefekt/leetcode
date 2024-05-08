class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # add indexes to scores
        scores = []
        for i,s in enumerate(score):
            scores.append([s,i])
        scores.sort(reverse = True)

        res = [0] * len(scores)
        for i in range(len(scores)):
            if i == 0:
                res[scores[i][1]] = "Gold Medal"
            elif i == 1:
                res[scores[i][1]] = "Silver Medal"
            elif i == 2:
                res[scores[i][1]] = "Bronze Medal"
            else:
                res[scores[i][1]] = str(i + 1)
    

        
        return res
