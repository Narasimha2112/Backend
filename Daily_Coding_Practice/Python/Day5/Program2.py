# Write multiple lines using a loop

with open("Daily_Coding_Practice\Day5\demo.txt", "a") as f:
    for i in range(6, 10):
        f.write(f"Line {i}\n")