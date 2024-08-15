"""

The file_manager class takes in a file path and allows you to read
write, append, or create a new file in Python. 

"""

import shutil 


class FileManager:
    def __init__(self,file_name):
        """
        Constructing a base template for a file manager.
        """
        self.file_name = file_name
        
    def read_file(self):
        """
        Opens and reads the file owned by the file manager.
        """

        # Go back and use the actual file object
        file_content = open(self.file_name, "r")
        file_text = file_content.read()
        return file_text
    
    def write_file(self, input_text):
        """
        Allows you to write to a file 

        """
        file_writer = open(self.file_name, "a")
        file_writer.writelines(input_text)
        return "Wrote to file successfully"

    # def append_file(self):
    #     """
# Append two files together *take special care here
    #     """
    #     open_file(self.file_name, "a")
    
    # def create_file (self):
    #     """
    #     Creates a new empty file

    #     """
    #     open_file(self.file_name, "x")


# # Get back to this
#     def copy_file(self, destination):
#         """
#         Copies a source file to the destination file. 
#         Source and destination files should be two different 
#         files with same extension.

#         """
#         source_file = open_file(self.file_name, "rb")
#         destination = open_file(self.file_name, "wb")
#         shutil.copyfileobj(source_file, destination_file)