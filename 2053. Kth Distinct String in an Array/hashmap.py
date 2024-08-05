class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # get counter to get unique vals
        counter = collections.Counter(arr)
        unique = set()
        for key,v in counter.items():
            if v == 1:
                unique.add(key)
        
        unique_arr = []
        for s in arr:
            if s in unique:
                unique_arr.append(s)
        
        if k > len(unique_arr):
            return ""
        return unique_arr[k-1]
