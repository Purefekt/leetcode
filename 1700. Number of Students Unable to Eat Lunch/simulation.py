"""
Simulation.
Run while loop till students array exists and students array != the previous state of students array.
The second condition is useful is checking, since if there is no change in students array, that means no student wants the top sandwich.
This means all numbers in students are either all 1s or all 0s.
If students[0] == sandwiches[0], pop from left for both.
Else, append the 0th student to students and pop from left.
Finally return length of students, these are the remaining students.

O(n+m) time is using a deque, since poping from left is O(1).
O(n) space used by previous array.
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        prev = []
        while students and students != prev:
            prev = students[::]
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
        
        return len(students)
        