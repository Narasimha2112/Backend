#JSON: Load employee data

import json

with open("Daily_Coding_Practice/Day8/emp.json", "r") as f:
    emp = json.load(f)
    
print(emp)
