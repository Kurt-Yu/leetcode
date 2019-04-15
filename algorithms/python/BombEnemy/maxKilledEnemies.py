def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    if not grid: return 0
    n, m = len(grid), len(grid[0])
    rowhits, colhits = 0, [0] * m
    res = 0
    
    for i in range(n):
        for j in range(m):
            if j == 0 or grid[i][j-1] == 'W':
                rowhits = 0
                for k in range(j, m):
                    if grid[i][k] == 'W': break
                    if grid[i][k] == 'E': rowhits += 1
            if i == 0 or grid[i-1][j] == 'W':
                colhits[j] = 0
                for k in range(i, n):
                    if grid[k][j] == 'W': break
                    if grid[k][j] == 'E': colhits[j] += 1
            if grid[i][j] == '0':
                res = max(res, rowhits + colhits[j])
    return res