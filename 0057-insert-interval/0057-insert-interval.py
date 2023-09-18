import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s1=bisect_left([item[0] for item in intervals],newInterval[0])
        s2=bisect_left([item[1] for item in intervals],newInterval[0])
        e1=bisect_right([item[0] for item in intervals],newInterval[1])
        e2=bisect_right([item[1] for item in intervals],newInterval[1])
      
        
        if s1==s2==e1==e2:
            return intervals[:s1]+[newInterval]+intervals[s1:]
        else:
            new_start=min(intervals[s2][0],newInterval[0])
            if e1!=e2:
                new_end=max(intervals[e2][1],newInterval[1])
            else:
                new_end=newInterval[1]
            return intervals[:s2]+[[new_start,new_end]]+intervals[e1:]
        
                