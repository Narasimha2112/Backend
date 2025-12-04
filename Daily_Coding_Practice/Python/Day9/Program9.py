# Replace multiple spaces with single space

import re

text = "Python     Backend     Developer"
print(re.sub(r"\s+", " ", text))