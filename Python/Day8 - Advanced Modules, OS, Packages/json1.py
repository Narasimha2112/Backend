#Convert Python → JSON (dump)
import json

data = {
    "name": "Venkat",
    "age": 22,
    "skills": ["Python", "SQL"]
}

json_text = json.dumps(data, indent=4)
print(json_text)
