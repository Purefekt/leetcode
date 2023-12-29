"""
Double linked list. Draw it to work it out.
Maintain a hashmap which stores key and the value is a reference to a ListNode. The ListNode has -> (key, val, next, prev).
So for the kv pair 1,1 -> the hashmap looks like {1 -> (1,1)} where (1,1) is a reference to the ListNode.
Initialize the DLL with a sentinel head and tail set as (-1,-1). The head and tail always point to these 2 nodes. The head is the lru and tail is the mru.
Create helper methods eject and add.
Eject will eject a node from the list. This can be done by getting the reference to the node using the key from the hashmap and then getting the prev and next nodes to it in the list. Then basically skipping this node by changing the prev.next and next.prev.
Add always adds a node to the mru or tail of the list. This is done by having the reference to the tail and also the element just prev to tail. Set the tail.prev to the new node and set the previous tail.prev's next to the node.
Get returns -1 if the key doesnt exists. If it does then that node needs to be shifted to mru. Eject the node and then add it back to the list. Return the value from node.val.
For Put, if key is not in cache, create a new node and add it. If key is in cache then change the value and then eject the node and add it back.
After adding/updating, check the size of hashmap, if > capacity, get the lru_node which is at head.next and then eject it. Also delete the corresponding kv pair from the hashmap.

O(1) time for get and put operations.
O(capacity) space for the hashmap.
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # create 2 sent nodes. One always stays at the head(lru) and one stays at tail (mru).
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        # connect them
        self.head.next = self.tail
        self.tail.prev = self.head 


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # get the ref to the node using hashmap
        node = self.cache[key]
        # eject this node
        self.eject(node)
        # add this node to mru
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.cache[key] = node
            self.add(node)
        else:
            # update the value. Eject the node and add it to mru
            self.cache[key].val = value
            node = self.cache[key]
            self.eject(node)
            self.add(node)
        
        # eject lru if size of hashmap > capacity. Also remove the kv pair from the hashmap
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.eject(lru_node)
            del self.cache[lru_node.key]

    
    def eject(self, node):
        # eject a node by setting its prev -> node.next and setting its next -> node.prev.
        prev_neighbor = node.prev
        next_neighbor = node.next
        prev_neighbor.next = node.next
        next_neighbor.prev = node.prev
    
    def add(self, node):
        # place this node at the tail (MRU). Need both tail node and the node before tail node. ie sent tail node and actual mru node.
        current_mru_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        current_mru_node.next = node
        node.prev = current_mru_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)