#Pathlib: List only folders
from pathlib import Path

for item in Path(".").iterdir():
    if item.is_dir():
        print(item)