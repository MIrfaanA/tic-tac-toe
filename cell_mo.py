class Cell:
  
    def __init__(self, x_coord: str, y_coord: str):
        """Give a description of what a contructor is, as well as how you are using it here."""
        self.x_coord = x_coord
        self.y_coord = y_coord
        # Randomly assign self.value to X, O or .
        self.value = "."

    def set_value (self, value):
      self.value = value
      return "Value set correctly"

    def get_value (self):
      return self.value
    
    # Write a validater to check that the value is correct (X or O or .)
      
        
        
