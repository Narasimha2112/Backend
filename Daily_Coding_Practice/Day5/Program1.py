# Write a program to open a file and count lines

count = 0

with open("Daily_Coding_Practice\Day5\demo.txt", "r") as f:
    for _ in f:
        count += 1
        
print(f"Total Lines: {count}")