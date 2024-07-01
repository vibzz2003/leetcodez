class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3], [6,9]]
        #newinterval = [2,5]
        # if newinterval[0] < intervals[i][1]:
        # newinterval[1] > intervals[i][1] and newinterval[i] < intervals[i+1][0]:
        # intervals[i][0] = min(newinterval[0], interval[i][0])
        #intervals[i][1] = max(newinterval[1], intervals[i][1])
        #else : i+=1

        result = []
        i = 0
        n = len(intervals)

        #checking intervals less than the new interval
        while i<n and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i+=1

        #checking the case where the condition becomes true and we have to merge the intervals
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        #adding the merged intervals
        result.append(newInterval)

        #adding the rest
        while i<n:
            result.append(intervals[i])
            i+=1


        return result

        