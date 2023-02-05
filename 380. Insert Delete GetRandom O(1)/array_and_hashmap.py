"""
Use a hashmap and an array
When we Insert an item, append it to the end of the array and add it to the hasmap with its value being its index (len(array))
To delete, we will get the array index of the val to be removed using the hasmap. Then get the last element of the array and place it into the index of the val to be deleted. Next update the index of the last element in the array in the hashmap to this new index and finally pop from the end of the array
To get random use random.choice(array) which returns a random element in O(1) time

O(1) time for all functions
O(n) space to store at max n elements at once in the hashmap and the array
"""

class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            n = len(self.array)
            self.array.append(val)
            self.hashmap[val] = n
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            # get the array index of the val to be removed from the hashmap
            # get the last element in the array and place it in the position of element to be removed, update the hashmap
            delete_idx = self.hashmap[val]
            self.array[delete_idx] = self.array[-1]
            self.hashmap[self.array[-1]] = delete_idx

            del self.hashmap[val]
            self.array.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()