from collections import deque
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ncol = len(grid[0])
        nrow = len(grid)
        dp = [[float('inf') for col in range(ncol)] for row in range(nrow)]
        dp[0][0]=grid[0][0]
        
        for i in range(1,ncol):
            dp[0][i] =grid[0][i]+dp[0][i-1]
        for j in range(1,nrow):
            dp[j][0] =grid[j][0]+dp[j-1][0]

        ##dp[i][j] = min(dp[i][j-1],dp[j-1][i])+grid[i][j]
        
        for j in range(ncol):
            for i in range(nrow):
                if i+1 >=nrow or j+1 >= ncol:
                    continue
                else :
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j])+grid[i+1][j+1]

        return dp[-1][-1]