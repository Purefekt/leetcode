"""
Use meeting rooms 2 to find the max number of rooms needed at a time.
If the number of rooms needed are > 2, return False and remove recently added interval.

O(nlogn) time for each call of book. We sort intervals in nlogn time and then run meeting rooms 2 by sorting again and then running in n time.
O(n) space used by sorted array.
"""

class MyCalendarTwo:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        self.intervals.append((start,end))

        # run meetings rooms 2 to get max numbers of meetings at a time
        count = 0
        cur = 0
        starts = [s for s,e in self.intervals]
        ends = [e for s,e in self.intervals]
        starts.sort()
        ends.sort()
        p1, p2 = 0, 0
        while p1 < len(starts):
            if starts[p1] < ends[p2]:
                cur += 1
                count = max(count, cur)
                if count > 2:
                    self.intervals.pop()
                    return False
                p1 += 1
            else:
                cur -= 1
                p2 += 1
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)