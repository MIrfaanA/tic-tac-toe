from cell import Cell

cell_1 = Cell(x_coord="1", y_coord="3")
cell_2 = Cell(x_coord="3", y_coord="2")


cell_1.WhereAmI()

cell_2.WhereAmI()


print(cell_1)


def distance(c1: Cell, c2: Cell):
    print("HERE")




distance(cell_1, cell_2)