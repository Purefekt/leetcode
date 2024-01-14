"""
Add the points and their frequency to a hashmap.
For count, create a list of all points with which the current points makes a vertical edge.
So go through all points in frequency map and add all points where the y axis is the same. NOTE: do not add if points are the same.
Iterate over all of these points, these are the point2.
For each point and point2 pair, get the vertical distance. Based on this distance, we can get the exact coordinates of the other 2 points which will make the square.
We can get 2 points on the left of current edge and 2 points to the right.
If these new points, point3 and point4 exist in the frequency hashmap, add the product of frequencies of point2 * point3 and point4 to result.

O(n) time for count where n is the number of points already added.
O(n) space for the frequency hashmap.
"""

class DetectSquares:

    def __init__(self):
        self.freq = collections.defaultdict(int)    

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        # get all points where point's y axis and another point's y axis are same
        all_point2 = []
        for k in self.freq:
            if tuple(point) != k:
                if (point[1]) == k[1]:
                    all_point2.append(k)
        
        res = 0
        for point2 in all_point2:
            distance = abs(point[0] - point2[0])
            
            # try to build squares on the left side
            point3 = (point[0], point[1] - distance)
            point4 = (point2[0], point2[1] - distance)
            if point3 in self.freq and point4 in self.freq:
                res += (self.freq[point2] * self.freq[point3] * self.freq[point4])
            
            # try to build squares on the right side
            point3 = (point[0], point[1] + distance)
            point4 = (point2[0], point2[1] + distance)
            if point3 in self.freq and point4 in self.freq:
                res += (self.freq[point2] * self.freq[point3] * self.freq[point4])
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)