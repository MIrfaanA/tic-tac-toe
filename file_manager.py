"""

The file_manager class takes in a file path and allows you to read
write, append, or create a new file in Python. 

"""

import shutil 

Class file_manager:
    def __init__(self,file_name):
        """
        returns file name and mode

        """
        self.file_name = filename
    

    def read_file(self):
        """
        Opens a specified file 

        """
        open_file(self.file_name, "r")
    
    def write_file(self):
        """
        Allows you to write to a file 

        """
        open_file(self.file_name, "w")

    def append_file(self):
        """
        Append to a file with the same extension type      

        """
        open_file(self.file_name, "a")
    
    def create_file (self):
        """
        Creates a new empty file

        """
        open_file(self.file_name, "x")

    def copy_file(self, destination):
        """
        Copies a source file to the destination file. 
        Source and destination files should be two different 
        files with same extension.

        """
        source_file = open_file(self.file_name, "rb")
        destination = open_file(self.file_name, "wb")
        shutil.copyfileobj(source_file, destination_file)