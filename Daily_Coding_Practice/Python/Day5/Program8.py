#Count Characters in a file

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as f:
    text = f.read()
    
print("Characters:", len(text))