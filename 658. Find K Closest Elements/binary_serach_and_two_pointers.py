"""
Use Binary search to find the index of the number closest to x in the array
Then use 2 pointers l and r and keep adding closest numbers till size k
special cases: if x is smaller than the smallest number then return the first k numbers
if x is larger than the largest number then return the last k numbers

O(logn + k) time. O(logn) to find the mid index and O(k) to run 2 pointers
O(1) space to track l,r,mid
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        res = collections.deque()
        # if x is smaller than the smallest or larger than the largest
        if x < arr[0]:
            for i in range(k):
                res.append(arr[i])
            return res
        if x > arr[-1]:
            for i in range(len(arr)-1, len(arr)-k-1, -1):
                res.appendleft(arr[i])
            return res
        
        # if x is somewhere within the range
        l = 0
        r = len(arr)-1
        p = None
        while l<=r:
            p = (l+r)//2
            if arr[p] == x:
                l = r = p
                break
            elif arr[p] > x:
                r = p-1
            else:
                l = p+1
        
        # get the midpoint index by if l is closer to x or r
        mid_idx = None
        print(l,r,p)
        if l==r:
            mid_idx = l
        else:
            if abs(arr[l]-x) < abs(arr[r]-x):
                mid_idx = l
            else:
                mid_idx = r
        
        # use 2 pointers from the midpoint to get all the numbers till size k
        l = mid_idx-1
        r = mid_idx+1
        res.append(arr[mid_idx])
        for _ in range(k-1):
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.appendleft(arr[l])
                l -= 1
            else:
                if x-arr[l] <= arr[r]-x:
                    res.appendleft(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
        
        return res
        