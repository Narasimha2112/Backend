#Find all 3-digit numbers

import re

text = "123, 45, 45, 678, 0"
print(re.findall(r"\b\d{3}\b", text))