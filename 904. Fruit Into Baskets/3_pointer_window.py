"""
3 Pointer sliding window
Keep a pointer 'l' for left end of sliding window. Pointer 'r' for right end of sliding window and a pointer 'start_t2' to cache the position where a 2nd type of fruit was placed in the bucket for the first time.
Start with all at 0 and our bucket has one kind of fruit, fruit[0]
Run a loop till 'r' stays within the length of the fruit array
If at a given position, fruits[r] is in the bucket, we increment r by 1
If at a given position, fruits[r] is not in the bucket, there can be 2 cases, the bucket has space for 1 more type of fruit or the bucket cannot hold any new type of fruit
In the first case, we will add the new type of fruit to the bucket and set that position as the first time we added the 2nd type of fruit
In the second case, we see the number of fruits we have in total. Now we move the sliding window by discarding all fruits before the 2nd type of fruit the first time
Thus we set l and r to start_t2 and repeat

O(n) time. In the worst case, all fruits are different, we will run the while loop 2n times
O(1) space. The bucket set will hold at max 2 elements, and constant space for l,r,s,num
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        bucket = set()    
    
        l = 0
        r = 0
        start_t2 = 0
        bucket.add(fruits[l])
        max_num = 0
        
        while r<len(fruits):
            
            if fruits[r] in bucket:
                r += 1
            
            else:
                if len(bucket) == 1:
                    bucket.add(fruits[r])
                    start_t2 = r
                    r += 1
                else:
                    num = r-l
                    max_num = max(max_num, num)
                    l = start_t2
                    r = start_t2
                    bucket.clear()
                    bucket.add(fruits[l])
                    r += 1
        
        # one last num when r goes beyond the length
        num = r-l
        max_num = max(max_num, num)
        
        return max_num
    