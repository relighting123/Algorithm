class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n,dp =len(obstacleGrid),len(obstacleGrid[0]), {}
        dp[(0,0)]=1
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col]==1: 
                    dp[(row,col)]=0
                    continue
                if row==0 and col==0:
                    dp[(0,0)]=1
                    continue
                if row==0 and col>0:
                    dp[(row,col)]=dp[(row,col-1)]
                    continue
                if col==0 and row>0:
                    dp[(row,col)]=dp[(row-1,col)]
                    continue
                
                    
                    
                dp[(row,col)]=dp[(row-1,col)]+dp[(row,col-1)]
        return dp[(m-1,n-1)]
                