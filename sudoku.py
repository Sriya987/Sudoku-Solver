def print_grid(grid):
    for row in grid:
        for num in row:
            if num==0:
                print('.',end=' ')
            else:
                print(num,end=' ')
        print()
def is_safe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if grid[i][j] == num:
                return False
    return True
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num 
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  
                return False 
    return True
sudoku_grid = [
    [0, 7, 0, 0, 2, 0, 0, 4, 6],
    [0, 6, 0, 0, 0, 0, 8, 9, 0],
    [2, 0, 0, 8, 0, 0, 7, 1, 5],
    [0, 8, 4, 0, 9, 7, 0, 0, 0],
    [7, 1, 0, 0, 0, 0, 0, 5, 9],
    [0, 0, 0, 1, 3, 0, 4, 8, 0],
    [6, 9, 7, 0, 0, 2, 0, 0, 8],
    [0, 5, 8, 0, 0, 0, 0, 6, 0],
    [4, 3, 0, 0, 8, 0, 0, 7, 0]
]
print("Original Sudoku Puzzle:")
print_grid(sudoku_grid)
if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku Puzzle:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
