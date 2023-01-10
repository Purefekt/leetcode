"""
If the length of nums is itself not a multiple of k, it cannot be valid
Create a frequency hashmap of all nums
Get the list of all keys (unique nums) and put them in a minheap, to access the smallest element
Run a loop till minheap lasts, the top element will be the start
Run a loop k number of times. If at any point the next consecutive number is NOT in the hashmap or its frequency is NOT 0, it is valid
Each time also decrement the frequency of that number by 1 and if at any point its frequency becomes 0, pop from the minheap so as to avoid using it again

O(nlogn) time. We could potentially pop n times from the minheap which takes logn time
O(n) space to store the minheap
"""

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        # if number of cards is not a multiple of groupSize, return False
        if len(nums) % k != 0:
            return False
        
        # get freq of all cards
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        # put all the keys into a minheap
        minheap = list(freq.keys())
        heapq.heapify(minheap)

        # try to make pairs till heap lasts
        while minheap:
            start = minheap[0]

            for i in range(k):
                if start+i not in freq:
                    return False
                if freq[start+i] <= 0:
                    return False
                freq[start+i] -= 1
                if freq[start+i] == 0:
                    heapq.heappop(minheap)

        return True
