#Read file and count words

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as f:
    text = f.read()
    
words = text.split()
print("Word Count:", len(words))
