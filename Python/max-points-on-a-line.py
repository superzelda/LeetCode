# Time:  O(n^2)
# Space: O(n)
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#

import collections


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution3(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import numpy
        res = 0
        for i in range(len(points)):
            same = 0
            dic = {'i': 1}
            for j in range(i+1, len(points)):
                dx, dy = points[j].x, points[j].y
                if dx == points[i].x and dy == points[i].y:
                    same += 1
                    continue
                if dx == points[i].x:
                    slope = 'i'
                else:
                    slope = (dy - points[i].y) *numpy.longdouble(1) / (dx - points[i].x)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            res = max(res, max(dic.values())+same)
        return res
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_points = 0
        for i, start in enumerate(points):
            slope_count, same = collections.defaultdict(int), 1
            for j in xrange(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    slope = float("inf")
                    if start.x - end.x != 0:
                        slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    slope_count[slope] += 1

            current_max = same
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)

            max_points = max(max_points, current_max)

        return max_points

if __name__ == "__main__":
    print Solution().maxPoints([Point(), Point(), Point()])
