"""
Find the rotation index
determine what side to search for and get l and r
binary search in that part
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        def find_rotation_index(l,r):
            if nums[r] > nums[l]:
                return 0
            
            while l<=r:
                pivot = l + ((r-l)//2)
                # if the pivot element is larger than the next element,this means the next element is the smallest
                if nums[pivot] > nums[pivot+1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[l]:
                        r = pivot - 1
                    else:
                        l = pivot + 1
        
        # get which side the answer might lie
        rotation_index = find_rotation_index(0, len(nums)-1)
        if nums[rotation_index] <= target <= nums[len(nums)-1]:
            l = rotation_index
            r = len(nums)-1
        elif nums[0] <= target <= nums[rotation_index-1]:
            l = 0
            r = rotation_index-1
        else:
            return -1
        
        # run binary search on the correct side
        while l<=r:
            pivot = l + ((r-l)//2)
            
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                l = pivot+1
            else:
                r = pivot-1
        return -1
    