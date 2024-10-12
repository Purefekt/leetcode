"""
2 heaps.
Create one heap called free, this is the chair numbers which are free.
Create another heap called cur, this stores the (exit time, chair number).
Add index to times and then sort it. we get ((start time, exit time), index).
Iterate over this, for each start and end time, we need to add it to cur by assigning it a chair.
But before that, we need to remove all friends whose exit time <= current start time.
We free those chairs and add them to free heap.
Now we can assign current friend a chair, we do this by either taking the top element from free heap.
If free is empty, this means we need to get the next chair which is the current size of cur.

O(nlogn) time for sorting and then heap ops.
O(n) space used by 2 heaps and sorting.
"""

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        # sort times with indexes
        time_idx = []
        for i,n in enumerate(times):
            time_idx.append((n, i))
        time_idx.sort()

        free = []
        heapq.heapify(free)
        cur = []
        heapq.heapify(cur)

        for time, idx in time_idx:
            s,e = time
            # eject all friends whose exit <= start of this friend. Add these chairs back to free
            while cur and cur[0][0] <= s:
                _, chair_num = heapq.heappop(cur)
                heapq.heappush(free, chair_num)
            # get the chair num to be assigned to this friend by taking the top element of free or the size of cur if no free chair exists
            this_chair = None
            if free:
                this_chair = heapq.heappop(free)
            else:
                this_chair = len(cur)
            # if this is target, then return
            if idx == targetFriend:
                return this_chair
            # else add to cur as (exit time, chair num)
            heapq.heappush(cur, (e, this_chair))
        