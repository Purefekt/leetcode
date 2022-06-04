class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Take XOR of all nums, the result will be the single nums. 
        # a XOR a == 0
        # a XOR 0 == a
        # suppose we have [a,b,b] => a XOR b XOR b, the last 2 will become 0 and a XOR 0 == a
        
        result = 0
        
        for n in nums:
            result = result ^ n
        
        return result