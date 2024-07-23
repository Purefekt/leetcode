class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        hashmap = collections.defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        arr = [(v,k) for k,v in hashmap.items()]
        arr = sorted(arr, key=lambda x:x[1], reverse=True)
        arr = sorted(arr, key=lambda x:x[0])
        
        res = []
        for count,n in arr:
            for _ in range(count):
                res.append(n)
        
        return res
            