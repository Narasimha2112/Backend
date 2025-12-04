#Convert JSON -> Python(load)

import json

json_text = '{"name": "Venkat", "age": 22}'

data = json.loads(json_text)
print(data)