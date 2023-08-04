from collections import defaultdict
class Solution:
    def getslope(self,a,b):
        x1,y1= a[0],a[1]
        x2,y2= b[0],b[1]
        if x1==x2:
            slope = "vertical"
        elif y1==y2:
            slope = "horizontal"
        else:
            slope = (y2-y1)/(x2-x1)
        
        return slope
    
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        board = [[False]*n for _ in range(n)]
        ans=0
        candidates=defaultdict(int)
        for i in range(n):
            
            for j in range(i+1,n):
                board[i][j]=self.getslope(points[i],points[j])
                candidates[board[i][j]]+=1
           # print(candidates,ans)
            if len(candidates)>0:
                ans=max(ans,max(candidates.values())) 
            candidates=defaultdict(int)
 
                
        
        
       
        return ans+1
        
        