#Count How many folders exist in directory

import os

count = len([d for d in os.listdir() if os.path.isdir(d)])
print(count)

print(os.listdir())