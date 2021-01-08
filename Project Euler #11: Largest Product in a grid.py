grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

rowp = [grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3] for j in range(17) for i in range(20)] # vertical products
colp = [grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j] for j in range(20) for i in range(17)]  # horizontal products
d1 = [grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3] for j in range(17) for i in range(17)] # left to right diagonal products
d2 = [grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3] for j in range(17) for i in range(17)]  # right to left diagonal products
print(max(max(rowp),max(colp),max(d1),max(d2)))  # max of all products
