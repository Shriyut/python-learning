# open("/home/sunny/PycharmProjects/python-learning/Basics/files/sample_file.txt")

# by default python will look for the file in the same directory as the script being executed
# sample_file = open("sample_file.txt", "r")
# sample_file.close()
# incase of errors the above approach can lead to data loss as file wouldnt be properly closed

# using with clause provides automatic cleanup
with open("sample_file.txt", "r") as file:
    content = file.read()
    print(content)


with open("new_file.txt") as file:
    for line in file:
        print(line.rstrip()) # just print function adds a line break at the end of the file