"""
Area = (1/2) * |x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)|
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        res = 0
        for a in range(len(points)):
            for b in range(a+1, len(points)):
                for c in range(b+1, len(points)):
                    res = max(res, 0.5 * abs(points[a][0] * (points[b][1] - points[c][1]) + points[b][0] * (points[c][1] - points[a][1]) + points[c][0] * (points[a][1] - points[b][1])))
        
        return res
