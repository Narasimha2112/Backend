# Extract domain from email

import re

email = "user@gmail.com"

domain = re.findall(r"@(.+)", email)

print(domain[0])