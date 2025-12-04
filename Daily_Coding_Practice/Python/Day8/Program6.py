#JSON: Save employee data to file
import json

emp_data = {"name": "Raj", "salary":3000}

with open("emp.json", "w") as f:
    json.dump(emp_data, f, indent=4)