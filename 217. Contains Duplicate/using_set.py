class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # using a set
        checking_set = set()
        
        for n in nums:
            if n in checking_set:
                return True
            checking_set.add(n)
        
        return False