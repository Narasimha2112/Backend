#Remove special characters

import re

text = "hello@python#123!"

clean = re.sub(r"[^A-Za-z0-9 ]", "", text)

print(clean)