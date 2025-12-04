#Split string on multiple delimiters

import re

text = "one;two:three|four"

print(re.split(r"[,:|;]", text))