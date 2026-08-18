class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        # add all intervals before start of new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # combine intervals if necessary for the new newinterval
        # keep merging while the start of each interval is less than end of newinterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # add all intervals after end of new interval
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res