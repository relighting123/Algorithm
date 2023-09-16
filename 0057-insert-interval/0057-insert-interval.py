import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s1=bisect_left([item[0] for item in intervals],newInterval[0])
        s2=bisect_left([item[1] for item in intervals],newInterval[0])
        e1=bisect_right([item[0] for item in intervals],newInterval[1])
        e2=bisect_right([item[1] for item in intervals],newInterval[1])
        print(s1,s2,e1,e2)
        
        #case1. s1,s2,e1,e2가 모두 동일한 경우 s1 인덱스에 new Intervals을 insert 처리
        #case2. s1-s2==1이면 s2인덱스의 범위 내 newintervals의 end point가 위치함.
        #case3. e1-e2==1이면 e2인덱스의 범위 내 newintervals의 end point가 위치함.
        #case4. s1==s2이면 s1인덱스의 시작점보다 newintervals의 시작점이 작아 시작점대체 가능
        #case5. e1==e2이면 e1-1의 인덱스의 끝점보다 newintervals의 end point가 더 커서 끝점 대체 가능
        
        if s1==s2==e1==e2:
            return intervals[:s1]+[newInterval]+intervals[s1:]
        else:
            if e1>e2:
                return intervals[:s2]+[[min(intervals[s2][0],newInterval[0]),max(intervals[e2][1],newInterval[1])]]+intervals[e2+1:]
            else:
                return intervals[:s2]+[[min(intervals[s2][0],newInterval[0]),newInterval[1]]]+intervals[e2:]
        
                