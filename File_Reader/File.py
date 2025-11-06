class File_class:
    def file_reader(self):
        with open("file.txt", "r") as file:
            print(file.read())
        
    def file_writer(self):
        with open("file.txt", "w") as file:
            file.write("Hello World")
    
    def file_appender(self):
        with open("file.txt", "a") as file:
            file.write("Hello World")
    
    def file_closer(self):
        with open("file.txt", "r") as file:
            print(file.read())
            file.close()
    
    def file_closer(self):
        with open("file.txt", "r") as file:
            print(file.read())
            file.close()

file = File_class()
file.file_reader()
file.file_writer()
file.file_appender()
file.file_closer()
file.file_closer()

