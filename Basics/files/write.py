file_name = "new_file.txt"

with open(file_name, "w") as file:
    file.write("new file \n") # creates or overwrites
    file.write("second line")