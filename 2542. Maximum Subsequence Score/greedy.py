"""
Greedy.
We need to maximize the sum in nums1 and maxmimize the min value from nums2.
Sort both array in descending order based on nums2.
Now we will try to set each value in nums2 as min and check the max score we can get.
This is done by setting current index in nums2 to op2 (min from nums2) and then getting the k-1 highest numbers from nums1.
Since we have sorted in desc order, we will build a minheap as we iterate and only use the values from the minheap, this way we avoid taking values from nums1 which are not valid, for example we if we set op2 = 3, this means we need to maintain 3 as the min in nums2, so we cannot take the corresponding element from nums1 which has a nums1 value of < 3.
After sorting, iterate through the pairs.
Set current nums2[i] to op2.
op1 begins with nums1[i], since the sum HAS to have this value.
Pop from the minheap first, this is removing the smallest currently seen value (all seen values will move in descending order of nums2).
Now add nums1[i] to it.
Calculate sum and get op1 * op2 and update res.

O(nlogn) time to sort. 
O(n) for storing sorted array.
"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # sort based on nums2
        nums = []
        for i in range(len(nums1)):
            nums.append((nums1[i], nums2[i]))
        nums.sort(key = lambda x: x[1], reverse=True)
        
        res = 0
        minheap = []
        heapq.heapify(minheap)
        op1 = 0
        for i in range(len(nums1)):
            op1 += nums[i][0]
            op2 = nums[i][1]
            # if heap size is k, remove the smallest nums1 element since we want to maximize it
            if len(minheap) == k:
                op1 -= heapq.heappop(minheap)
            # add the current nums1 element, to the heap since we HAVE to chose this nums1 value since we set this nums2 value as min
            heapq.heappush(minheap, nums[i][0])

            if len(minheap) == k:
                res = max(res, op1 * op2)
        
        return res
            