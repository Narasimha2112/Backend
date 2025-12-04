#Check the file is empty

import os

if os.path.getsize("Daily_Coding_Practice\Day5\demo.txt") == 0:
    print("Empty File")
else:
    print("Not Empty")

