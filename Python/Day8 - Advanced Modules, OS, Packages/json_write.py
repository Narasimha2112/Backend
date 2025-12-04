#Write json to file
import json

data = {'name': 'Venkat', 'age': 22}

with open("user.json", "w") as f:
    json.dump(data, f, indent=4)
