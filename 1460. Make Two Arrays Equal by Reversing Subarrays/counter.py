class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        counter_target = collections.Counter(target)
        counter_arr = collections.Counter(arr)

        for k,v in counter_target.items():
            if k not in counter_arr:
                return False
            if v != counter_arr[k]:
                return False
        
        return True
