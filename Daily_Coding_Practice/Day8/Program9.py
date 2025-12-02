#OS: Delete file only if exists
import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
else:
    print("File Not Exists...")