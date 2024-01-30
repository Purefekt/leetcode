"""
Create a hashmap where keys are the nums and values are list of indexes where it is found.
Can easily make this using enumeration.
For pick, get a random index between [0, len(values of that target)].
Return the value at this index.

O(n) time to for constructor to create the hashmap. O(1) time for pick since random number is generated in constant time.
O(n) space to store the hashmap. 
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.indexes = collections.defaultdict(list)
        for i,n in enumerate(nums):
            self.indexes[n].append(i)
        

    def pick(self, target: int) -> int:
        
        random_idx = random.randint(0, len(self.indexes[target])-1)
        return self.indexes[target][random_idx]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)