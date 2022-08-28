class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create a hashmap. The number required to create the target sum (target - number) is the key. Value is the index of this number
        hashmap = {}
        for i in range(len(nums)):
            hashmap[target-nums[i]] = i
        
        print(hashmap)
        
        # go through all numbers in nums. If it exists as a key in the dict, then the value will be the corresponding number index to get the target as sum
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                if i != hashmap[nums[i]]:
                    return i, hashmap[nums[i]]
            