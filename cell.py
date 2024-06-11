class Cell:
    def __init__(self, x_coord: str, y_coord: str):
        self.x_coord = x_coord
        self.y_coord = f"SOME RANDOM TEXT: {y_coord}"

    def WhereAmI(self):
        print(f"I am here: {self.x_coord}, {self.y_coord}")

# OOP Principles - TO DO
# 1. Create your own cell class
# 2. Set if it is X or O
# 3. Get the value
# 4. Get the coords as a dictionary
# 5. Create a grid class with an array of Cell objects




