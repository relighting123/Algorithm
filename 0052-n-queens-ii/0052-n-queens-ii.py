
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def dfs(row, visited):
            nonlocal ans
            if row == n:
                ans += 1
                return

            for col in range(n):
                valid = True

                for x, y in enumerate(visited[:row]):
                    if y== col or y + x == col + row or y - x == col - row:
                        valid = False
                        break
                if valid:
                    visited[row] = col
                    dfs(row + 1, visited)

        dfs(0, [-1] * n)
        return ans