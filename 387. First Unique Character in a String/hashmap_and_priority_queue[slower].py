import heapq

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # hashmap. key=letter, value=(index, count)
        
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap.keys():
                hashmap[s[i]] = [i, 1]
            else:
                hashmap[s[i]] = [i, hashmap[s[i]][1]+1]
        
        # create a priority queue where the count must be 1. Then heapify to get the smallest index
        priority_queue = []
        for k,v in hashmap.items():
            if hashmap[k][1] == 1:
                priority_queue.append(hashmap[k])
        
        # if no element appears exactly once, then this queue will be empty
        if len(priority_queue) < 1:
            return -1
        
        # min heapify this priority queue
        heapq.heapify(priority_queue)
        
        return priority_queue[0][0]
    