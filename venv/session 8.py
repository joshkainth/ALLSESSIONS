import os

path = os.getcwd()  # CWD -> Current Working Directory
print("path is : ",path)

print(os.name)
print(os.getlogin())
print(os.getppid()) # PPID -> Parent Process ID

path = "D:/Python Project/database_project/venv/MAIN_GUI.py"
print("is Path existing : ",os.path.exists(path))
print("Is path a directory : ",os.path.isdir(path))
print("Is path a file : ",os.path.isfile(path))

path = "D:/"

files = os.walk(path)
allfiles = list(files)  # Convert into a list
for file in allfiles:
    print(file)