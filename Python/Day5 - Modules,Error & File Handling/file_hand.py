#Opening a file & Write to file
f = open("demo.txt", "w") #creates file if not exists
f.write("Hello! This is JACK. \n")
f.write("Learning Python backend. \n")
f.close()

#Read a file
f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()


#Read line by Line
f = open("demo.txt", "r")

for line in f:
    print(line.strip())
    
f.close()


#Append to file
f = open("demo.txt", "a")
f.write("New line added.\n")
f.close()

#✔ Best practice: using with
# Automatically closes file.
with open("demo.txt", "r") as f:
    print(f.read())