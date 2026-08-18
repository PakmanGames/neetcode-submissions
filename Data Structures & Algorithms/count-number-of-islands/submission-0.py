class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        m * n array of bool to mark as seen or not seen --> start as all false # O(n * m) space

        outer loop to loop from 0 to len(grid) rows and o to len(grid[0]) cols

        queue = dequeue() # O(n * m) space
        rows = len(grid)
        cols = len(grid[0])

        double for loop to loop over each cell in grid # O(n * m)
        if grid[i][j] == 0: do nothing
        if grid[i][j] == 1 and seen[i][j] not true:
            num of islands += 1
            queue.append([i, j])
            while queue: # O(n * m)
                curr = queue.popleft()
                if i + 1 < rows and seen[i + 1][j] not true:
                    queue.append(grid[i + 1][j])
                if j + 1 < cols and seen[i][j + 1] not true:
                    queue.append(grid[i][j + 1])
        return res 

        # at first glance looks like O((n * m) ^ 2) but
        # AT MOST this algorithm checks each individual cell TWICE
        # O(2 * n * m) --> O(n * m) time complexity
        '''
        rows = len(grid)
        cols = len(grid[0])
        seen = [[] for _ in range(rows)]
        for i in range(rows):
            seen[i] = [False for _ in range(cols)]

        res = 0 # number of islands
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not seen[i][j]:
                    res += 1
                    queue.append([i, j])
                    while queue: # while queue is not empty
                        c_i, c_j = queue.popleft()
                        if c_i + 1 < rows and grid[c_i + 1][c_j] == '1' and not seen[c_i + 1][c_j]:
                            queue.append([c_i + 1, c_j])
                            seen[c_i + 1][c_j] = True
                        if c_j + 1 < cols and grid[c_i][c_j + 1] == '1' and not seen[c_i][c_j + 1]:
                            queue.append([c_i, c_j + 1])
                            seen[c_i][c_j + 1] = True
                        if c_i - 1 >= 0 and grid[c_i - 1][c_j] == '1' and not seen[c_i - 1][c_j]:
                            queue.append([c_i - 1, c_j])
                            seen[c_i - 1][c_j] = True
                        if c_j - 1 >= 0 and grid[c_i][c_j - 1] == '1' and not seen[c_i][c_j - 1]:
                            queue.append([c_i, c_j - 1])
                            seen[c_i][c_j - 1] = True
        return res