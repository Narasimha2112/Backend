import re

text = "Prices: 200, 499, 1578"

nums = re.findall(r"\d+", text)
print(nums)