"""
Store values in a hashmap with key=key : values = [(timestamp,value),...]
For every get operation, if the the timestamp is less than the smallest timestamp, then return
If the timestamp is larger than the largest timestamp then return the value of the last timestamp
Else run binary search to find the correct timestamp in the list in logN
If on running binary search we could not find the timestamp, then return the value of pivot-1 element

m = number of set calls
n = number of get calls
O(m) time for set
O(nlogm) time for get. logm to run binary search n times
O(l) space where l are the keys to store in a hashmap
"""

class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.time_map: return ""
        
        else:
            values_list = self.time_map[key]
            if timestamp < values_list[0][0]:
                return ""
            if timestamp > values_list[-1][0]:
                return values_list[-1][1]
            
            l = 0
            r = len(values_list)-1
            while l<=r:
                pivot = (l+r)//2
                if timestamp == values_list[pivot][0]:
                    return values_list[pivot][1]
                elif timestamp > values_list[pivot][0]:
                    l = pivot+1
                else:
                    r = pivot-1
            
            return values_list[pivot-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)