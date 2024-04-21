class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)  ]
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    
                    queue.append((row,col,0))
        t=0
        ans=0
        while queue:
            x,y,t=queue.popleft()
            ans=max(ans,t)
            for dx,dy in direction:
                nextx,nexty=x+dx,y+dy
                if nextx<0 or nexty<0 or nextx>=len(grid) or nexty>=len(grid[0]):
                    continue
                if grid[nextx][nexty]==1:
                    queue.append((nextx,nexty,t+1))
                    grid[nextx][nexty]=0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return -1
        return ans
                    
        
        