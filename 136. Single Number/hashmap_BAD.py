class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # linear time, linear space with hashmaps
        count_dict = {}
        
        # iterate over the list and inc the count of numbers
        for n in nums:
            if n not in count_dict.keys():
                count_dict[n] = 1
            else:
                count_dict[n] = count_dict[n] + 1
        
        # find the number appearing once and get its key
        for k,v in count_dict.items():
            if v == 1:
                return k