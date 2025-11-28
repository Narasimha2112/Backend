#Read file and convert all text to uppercase

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as f:
    text = f.read()
    
print(text.upper())