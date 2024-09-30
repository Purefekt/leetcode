"""
Similar to LRU cache.
Each node in the double linked list holds:
freq: frequency or count
prev: previous node
next: next node
members: set of strings which are of this given count.
Start by creating a max and min nodes with 0 as freq and connect them to each other.
The smallest frequency will be next of min and the highest frequency will be to the left of max.
At start we have (min) <=> (max).
We also keep a hashmap, whose keys are the strings and values are pointers to the nodes in the linked list.
For increment, if the node doesnt exist in the hashmap, this means its frequency will be 1.
Now check if the node to the right of min has freq 1 or not.
If it does not, then create a new node with freq 1 and add this string as members and inject it to the right of min.
If the node with freq 1 does exist, simply update the members of this node.
Now if the string already exist in the hashmap, we will have a pointer to the node which holds the current frequency of this string.
Check if cur_node.next.freq == current frequency + 1. This will confirm if we need to add a new node to the right of this node or update the members.
When we increment this way, we also remove a member from the current node since we moved it to the next node.
In this case if they current nodes members are 0, we need to eject that node from the linked list.
Do similar for decrement but in opposite direction.

O(1) time for all operations.
O(n) space used by the hashmap and nodes.
"""

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.members = set()

class AllOne:

    def __init__(self):
        self.min = Node(freq=0)
        self.max = Node(freq=0)
        self.min.next = self.max
        self.max.prev = self.min
        self.hashmap = {}
        
    def inc(self, key: str) -> None:
        if key not in self.hashmap:
            if self.min.next.freq != 1:
                new_node = Node(freq=1)
                new_node.members.add(key)
                self.hashmap[key] = new_node
                # inject this node to the right of min
                nxt_tmp = self.min.next
                self.min.next = new_node
                new_node.prev = self.min
                new_node.next = nxt_tmp
                nxt_tmp.prev = new_node
            else:
                node = self.min.next
                node.members.add(key)
                self.hashmap[key] = node
        else:
            cur_node = self.hashmap[key]
            if cur_node.next.freq != cur_node.freq + 1:
                new_node = Node(freq=cur_node.freq+1)
                new_node.members.add(key)
                cur_node.members.remove(key)
                self.hashmap[key] = new_node
                # inject this node to the right of cur node
                nxt_tmp = cur_node.next
                cur_node.next = new_node
                new_node.prev = cur_node
                new_node.next = nxt_tmp
                nxt_tmp.prev = new_node
            else:
                node = cur_node.next
                node.members.add(key)
                self.hashmap[key] = node
                cur_node.members.remove(key)
            # eject this node if size drops to 0
            if len(cur_node.members) == 0:
                prev_tmp = cur_node.prev
                nxt_tmp = cur_node.next
                prev_tmp.next = nxt_tmp
                nxt_tmp.prev = prev_tmp

    def dec(self, key: str) -> None:
        cur_node = self.hashmap[key]
        # if it decrements to 0, remove from hashmap
        if cur_node.freq == 1:
            del self.hashmap[key]
            cur_node.members.remove(key)
        else:
            if cur_node.prev.freq != cur_node.freq - 1:
                new_node = Node(freq=cur_node.freq-1)
                new_node.members.add(key)
                cur_node.members.remove(key)
                self.hashmap[key] = new_node
                # inject this node to the left of cur node
                prev_tmp = cur_node.prev
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = prev_tmp
                prev_tmp.next = new_node
            else:
                node = cur_node.prev
                node.members.add(key)
                self.hashmap[key] = node
                cur_node.members.remove(key)
        # eject this node if size drops to 0
        if len(cur_node.members) == 0:
            prev_tmp = cur_node.prev
            nxt_tmp = cur_node.next
            prev_tmp.next = nxt_tmp
            nxt_tmp.prev = prev_tmp

    def getMaxKey(self) -> str:
        if self.max.prev.freq == 0:
            return ""
        return next(iter(self.max.prev.members))
        

    def getMinKey(self) -> str:
        if self.min.next.freq == 0:
            return ""
        return next(iter(self.min.next.members))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()