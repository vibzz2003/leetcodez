class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        #sorting according to the last index of balloons 
        points.sort(key=lambda x:x[1])

        #initialising arrow count to 1
        arrows = 1

        #initialising current end to the end of first index
        current_end = points[0][1]

        for start, end in points[1:]:
            if start > current_end:
                arrows+=1
                current_end = end
        
        return arrows
