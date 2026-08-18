class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0

        seen = [[False for _ in range(cols)] for _ in range(rows)]
        # O(n*m) space to track spaces that have been seen

        # O(n*m) time to traverse the entire grid
        for i in range(rows):
            for j in range(cols):
                if not seen[i][j] and grid[i][j] == "1":
                    res += 1
                    self.searchIsland(i, j, grid, seen) # max is O(n*m) only once
        return res
                
    def searchIsland(self, i: int, j: int, grid: List[List[str]], seen: List[List[bool]]):
        rows = len(grid)
        cols = len(grid[0])
        changes = [(1, 0), (-1, 0), (0, 1), (0, -1)] # N, S, E, W
        queue = [(i, j)] # largest size is O(n*m)
        # AT MOST we would traverse every element in one method call O(n*m) time
        while queue:
            current = queue.pop()
            c_i = current[0]
            c_j = current[1]
            seen[c_i][c_j] = True
            for tup in changes:
                n_i = c_i + tup[0]
                n_j = c_j + tup[1]

                if n_i >= 0 and n_i < rows and n_j >= 0 and n_j < cols and not seen[n_i][n_j] and grid[n_i][n_j] == "1":
                    queue.append((n_i, n_j))
        return
        # Max time: O(2*n*m) --> O(n*m)
        # Space: O(n*m)