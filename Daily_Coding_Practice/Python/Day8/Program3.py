#Move all .txt files to a folder
from pathlib import Path
import shutil

folder = Path(".")
backup = Path("Backup")
backup.mkdir(exist_ok=True)

for f in folder.glob("*.txt"):
    shutil.move(str(f), backup)
