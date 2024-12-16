"""
Heap.
Create a maxheap with (-gain, pass, total) for each class in classes.
Gain is what we will get if we add 1 student to this class.
Simply (pass+1)/(total+1)  -  (pass/total).
This will help us pick the best class to add a student to with the max gain.
We repeat this extraStudents times.
Then we iterate over the heap to get the new pass ratio and divide that be len(classes).

O(nlogn) time where n is size of classes. Building the heap takes n times, then adding all students takes k time where k is size of extraStudents but k == n. Within that, heap operations take logn time.
O(n) space used by heap.
"""

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # create pq with (-gain, curr pass, curr total) to create maxheap
        def get_gain(cur_pass, cur_total):
            new_ratio = (cur_pass+1)/(cur_total+1)
            old_ratio = cur_pass/cur_total
            return new_ratio - old_ratio
        
        pq = []
        for p,t in classes:
            gain = get_gain(p,t)
            pq.append((-gain, p, t))
        heapq.heapify(pq)

        for _ in range(extraStudents):
            gain, p, t = heapq.heappop(pq)
            new_p = p + 1
            new_t = t + 1
            new_gain = get_gain(new_p, new_t)
            heapq.heappush(pq, (-new_gain, new_p, new_t))
        
        # now build result
        n = len(classes)
        ratios = 0
        for _, p, t in pq:
            ratios += (p/t)
        
        return ratios/n
