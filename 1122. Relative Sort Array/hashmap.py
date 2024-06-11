class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        indexes = {}
        for i,n in enumerate(arr2):
            indexes[i] = n
        
        # get freq of arr1
        freq = collections.defaultdict(int)
        for n in arr1:
            freq[n] += 1
        
        not_in_arr1 = list(set(freq.keys()) - set(arr2))
        not_in_arr1.sort()

        res = []
        for i in range(len(indexes)):
            num = indexes[i]
            for j in range(freq[num]):
                res.append(num)
        
        for num in not_in_arr1:
            for j in range(freq[num]):
                res.append(num)
        
        return res
