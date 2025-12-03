# Extract all words starting with capital letter

import re

text = "Venkat is Learning Python in India"

print(re.findall(r"\b[A-Z][a-z]", text))