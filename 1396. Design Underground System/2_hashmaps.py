"""
2 hashmaps.
Use a hashmap to track the users in transit. ID -> (start station, start time).
When a user checks out, fetch that user's start station and start time and delete it from the in transit hashmap.
Use a hashmap trip data to store the total time and total number of trips experiences by a combination of start and end station.
start station -> end station -> {time: int, trips: int}.
At checkout, increment time and trips.
At get average, calculate average using the trip data hashmap.

O(1) time. per call for hashmap operations. 
O(p + s^2) space where s is the number of stations and p is the number of passengers. O(p) is needed for in transit hashmap to hold all passengers if everyone is in transit at the same time. Station data is stored in trip data, each station can lead to every other station thus needing O(s*(s-1)) or O(s^2) space.
"""

class UndergroundSystem:

    def __init__(self):
        self.in_transit = {}
        self.trip_data = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_transit[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # get the customer's checkin station and time
        checkin_station, checkin_time = self.in_transit[id]
        del self.in_transit[id]

        # add checkin station to duration if not already present
        if checkin_station not in self.trip_data:
            self.trip_data[checkin_station] = {}
        # add the checkout station to checkin station's hashmap if not already present
        if stationName not in self.trip_data[checkin_station]:
            self.trip_data[checkin_station][stationName] = {
                'time': 0,
                'trips': 0
            }
        
        # add the time taken for this trip and increment the number of trips
        self.trip_data[checkin_station][stationName]['time'] += t - checkin_time
        self.trip_data[checkin_station][stationName]['trips'] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = self.trip_data[startStation][endStation]['time']
        total_trips = self.trip_data[startStation][endStation]['trips']

        return total_time / total_trips

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)