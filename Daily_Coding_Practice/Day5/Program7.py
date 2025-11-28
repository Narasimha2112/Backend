#Replace specific word in a file

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as f:
    text = f.read()
    
text = text.replace("Line", "Row")

with open("Daily_Coding_Practice\Day5\demo.txt", "w") as f:
    f.write(text)