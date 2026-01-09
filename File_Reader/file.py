# The file closes automatically when the indentation block ends
# with creating a context manager


with open("files.txt", "r") as file:
    print(file.read())



