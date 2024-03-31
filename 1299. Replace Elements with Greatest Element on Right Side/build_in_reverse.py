class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        cur_max = -1

        res = []
        for i in range(len(arr)-1, -1, -1):
            res.append(cur_max)
            cur_max = max(cur_max, arr[i])
        
        res = res[::-1]
        return res
        