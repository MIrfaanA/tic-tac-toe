# 3x3 = 9 cells
# Every cell has a X and Y coord. 

# game_board = [[1][2][3]
#               [4][5][6]
#               [7][8][9]]

from cell_mo import Cell

c1 = Cell(x_coord=1, y_coord=1)
c2 = Cell(x_coord=2, y_coord=1)

grid = []

# grid = [
#     [Cell(1,1), Cell(1, 2), Cell(1, 3)],
#     [Cell(2,1), Cell(2, 2), Cell(2, 3)],
#     [Cell(3,1), Cell(3, 2), Cell(3, 3)],
# ]

row = 3
col = 3


for r in range(row):
    for c in range(col):
            print(f"{r}:{c}")
            grid.append(Cell(r, c))


# Next Step:
# - Document your class with all its functions.
# - Create a 100x100 game grid that is:
    # An array of arrays.
        # (See line 15)
        # To Access a cell at 1:2: grid[1][2]
# - Create a for loop that outputs a structured game board
# - Write that output to a text file.

print("x_coord\t\ty_coord")
