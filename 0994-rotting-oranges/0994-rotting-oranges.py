class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        time, fresh_orange = 0, 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    fresh_orange += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        locations = [(0,1), (1, 0), (0,-1), (-1, 0)]
        
        while queue and fresh_orange > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in locations:
                    new_x, new_y = x+dx, y+dy
                    if -1 < new_x < m and -1 < new_y < n:
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            queue.append((new_x, new_y))
                            fresh_orange -= 1
            time += 1
        # print(time)    
        return time if fresh_orange == 0 else -1 
        
        