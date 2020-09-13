class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if grid:
            n,m = len(grid), len(grid[0])
            visited = [[False for j in range(m)] for i in range(n)]
            def dfs(i,j):
                visited[i][j] = True
                if i < n-1 and grid[i+1][j] == '1' and not visited[i+1][j]:
                    dfs(i+1,j)
                if i > 0 and grid[i-1][j] == '1' and not visited[i-1][j]:
                    dfs(i-1,j)
                if j < m-1 and grid[i][j+1] == '1' and not visited[i][j+1]:
                    dfs(i,j+1)
                if j > 0 and grid[i][j-1] == '1' and not visited[i][j-1]:
                    dfs(i,j-1)
            for i in range(n):
                for j in range(m):
                    if not visited[i][j] and grid[i][j] == '1':
                        dfs(i,j)
                        count += 1
        return count
