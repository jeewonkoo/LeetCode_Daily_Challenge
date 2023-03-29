class Solution:
    def bfs(self, grid, x, y):
        queue = collections.deque()
        queue.append((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            for x_, y_ in directions:
                new_x, new_y = x_ + x, y_ + y
                if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]) and grid[new_x][new_y] == "1":
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = "0"
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    num_island+= 1
                    
        return num_island