#Copy content of one file to another

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as src:
    data = src.read()
    
with open("Daily_Coding_Practice\Day5\copy.txt", "w") as dest:
    dest.write(data)

    