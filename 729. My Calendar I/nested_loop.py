"""
Nested loop solution.
Check current interval against all intervals.
Intervals do not intersect if one of them start after the other ends.

O(n^2) time.
O(n) space used by intervals.
"""

class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        
        for si,ei in self.intervals:
            if si < end and start < ei:
                return False
        self.intervals.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)