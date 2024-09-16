import shutil

class FileManager:
    def __init__(self, file_name):
        """
        Constructing a base template for a file manager.
        """
        self.file_name = file_name

    def read_file(self):
        """
        Opens and reads the file owned by the file manager.
        """
        with open(self.file_name, "r") as file_content:
            file_text = file_content.read()
        return file_text
    
    def write_file(self, input_text):
        """
        Allows you to write to a file.
        """
        with open(self.file_name, "w") as file_writer:
            file_writer.writelines(input_text)
        return "Wrote to file successfully"

    def append_file(self, text_to_append):
        """
        Appends text to the end of the file.
        """
        with open(self.file_name, "a") as file_writer:
            file_writer.writelines(text_to_append)
        return "Appended to file successfully"
    
    def create_file(self):
        """
        Creates a new empty file. If the file already exists, it raises an error.
        """
        try:
            with open(self.file_name, "x") as file:
                pass
            return "File created successfully"
        except FileExistsError:
            return "File already exists"

    def copy_file(self, destination_path):
        """
        Copies the current file to a new destination.
        """
        shutil.copy(self.file_name, destination_path)
        return f"File copied to {destination_path} successfully"
