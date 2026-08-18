class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        seen = [[] for _ in range(row)]
        for i in range(row):
            seen[i] = [False for _ in range(col)]
        
        def dfs(i, j):
            if grid[i][j] != 1:
                return 0
            
            adj = [[-1, 0], [1, 0], [0, - 1], [0, 1]]
            a = 1
            for index in range(len(adj)):
                ni = i + adj[index][0]
                nj = j + adj[index][1]
                if ni >= 0 and ni < row and nj >= 0 and nj < col:
                    if grid[ni][nj] == 1 and not seen[ni][nj]:
                        seen[ni][nj] = True
                        a += dfs(ni, nj)
            return a
        
        area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not seen[i][j]:
                    seen[i][j] = True
                    area = max(area, dfs(i, j))
        return area