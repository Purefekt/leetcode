"""
Using three pointers. pointer for nums1 will be at the last valid number. pointer for nums2 will be the last element of the list nums2. A third pointer will point towards the index in nums1 which must be filled, pointer will be initialized at the end of the list nums1. We compare and fill the values from left to right and move the corresponding pointers. At a point, one of the two lists will be all used up, end the loop and fill the remaining elements in the other list as is since they are already sorted.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m_pointer = m-1
        n_pointer = n-1
        fill_pointer = m+n-1
        
        while (m_pointer >= 0 and n_pointer >= 0):
            
            # if nums2 is larger than nums1, then we add the larger number in the fill pointer index, since filling right to left, or largest to smallest
            if nums2[n_pointer] > nums1[m_pointer]:
                nums1[fill_pointer] = nums2[n_pointer]
                
                # update n_pointer and fill_pointer to move left. m_pointer is unchanged
                n_pointer -= 1
                fill_pointer -= 1
            
            # else if nums1 is larger than nums2, then we add nums1 in the fill pointer index
            else:
                nums1[fill_pointer] = nums1[m_pointer]
                
                # update
                m_pointer -= 1
                fill_pointer -= 1
        
        # this loop terminates when nums1 is used up. put the nums in nums2 to the fill pointer index one by one
        if m_pointer < 0:
            while n_pointer >= 0:
                nums1[fill_pointer] = nums2[n_pointer]
                
                # update
                fill_pointer -= 1
                n_pointer -= 1
                