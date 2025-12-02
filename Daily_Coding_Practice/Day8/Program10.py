#Create a log file and append timestamp
from datetime import datetime

with open("Daily_Coding_Practice/Day8/log.txt", "a") as f:
    f.write(str(datetime.now()) + "\n")