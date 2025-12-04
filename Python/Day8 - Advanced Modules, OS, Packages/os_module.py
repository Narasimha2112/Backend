import os

#Check current directory
print(os.getcwd())

#List files in a folder
files = os.listdir()
print(files)

#create folder
os.mkdir("test_folder")

#remove Folder
os.rmdir("test_folder")

#Rename file/folder
os.rename("test_folder", "new_test_folder")

#Check if file exists
if os.path.exists("demo.txt"):
    print("File Exists")
else:
    print("File Not Found.....")