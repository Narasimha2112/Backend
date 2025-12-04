from pathlib import Path

p = Path("demo.txt")

print(p.exists())  #True/False
print(p.is_file())  #True/False

#Read file using Pathlib
p = Path("data.txt")

content = p.read_text()
print(content)


#Write to file using Pathlib
p = Path("notes.txt")

p.write_text("Hello Backend Developer!")


#List all .txt files
folder = Path(".")
txt_files = folder.glob("*.txt")

for file in txt_files:
    print(file)


#create folder
Path("logs").mkdir(exist_ok=True)
