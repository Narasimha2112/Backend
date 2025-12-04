#Read JSON from file
import json
with open("Day8 - Advanced Modules, OS, Packages/user.json", "r") as f:
    data = json.load(f)
    
print(data)