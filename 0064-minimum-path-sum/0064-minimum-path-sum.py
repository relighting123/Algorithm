class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distance = [[float('inf')] * cols for _ in range(rows)]
        distance[0][0]=grid[0][0]
        dx,dy=[(1,0)],[(0,1)]
        queue = [(0,0)]
        
        while(queue):
            r, c = queue.pop(0)
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distance[r][c]+grid[nr][nc] < distance[nr][nc]:
                        distance[nr][nc] = min(distance[nr][nc],distance[r][c]+grid[nr][nc])
                        queue.append((nr,nc))

        return distance[-1][-1]
            
            
        