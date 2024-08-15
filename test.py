from file_manager import FileManager


bob = FileManager(file_name="BOB.txt")
fred = FileManager(file_name="FRED.txt")


bob_content = bob.read_file()
fred_content = fred.read_file()


print(bob_content)
print(fred_content)


res  = fred.write_file("HERE IS A DEMO FOR MO")

file_length = 10 # characters

file_length = bob_content



# Get the content of bob
# Get the content of the destination file
# Write bob into destination (appending)


destination_fm = FileManager("destination.txt")
destination_content = destination_fm.read_file()

new_content = bob_content + destination_content

destination_fm.write_file(new_content)



