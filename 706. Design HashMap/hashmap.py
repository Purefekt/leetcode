"""
Bucket of size 2069
Use arrays for collisions
"""

class MyHashMap:

    def __init__(self):
        self.map = [None]*2069

    def put(self, key: int, value: int) -> None:
        hash_key = key%2069
        
        if not self.map[hash_key]:
            self.map[hash_key] = [[key,value]]
        else:
            for k_v_pair in self.map[hash_key]:
                if key == k_v_pair[0]:
                    k_v_pair[1] = value
                    break
            if [key,value] not in self.map[hash_key]:
                self.map[hash_key].append([key,value])
        

    def get(self, key: int) -> int:
        hash_key = key%2069
        
        if not self.map[hash_key]:
            return -1
        
        for k_v_pair in self.map[hash_key]:
            if key == k_v_pair[0]:
                return k_v_pair[1]
        
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = key%2069
         
        if self.map[hash_key]:
            for i in range(len(self.map[hash_key])):
                if key == self.map[hash_key][i][0]:
                    self.map[hash_key].pop(i)
                    break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)