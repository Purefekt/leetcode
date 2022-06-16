"""
set p1 to left end of the list
set p2 to right end of the list

if list[p1] + list2[p2], then return those indicies, have to change p2 from neg indicies to normal index
if the sum is larger than target, then move p2 left, since p1 and any number larger than p1 and p2 will still be larger than target
similarly if sum is smaller than target, move p1 to right
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1 = 0
        p2 = -1
        
        while(1):
            if numbers[p1] + numbers[p2] == target:
                # p2 has neg indicies, must change to normal
                p2 = p2 + len(numbers)
                
                return [p1+1, p2+1,]
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
        