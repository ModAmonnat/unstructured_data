#Count the number of files to ensure process all files correctly
from pathlib import Path

folder_path = r"D:\BCIT\Winter 2026\BI2\CS1\Dataset"
file_count = len(list(Path(folder_path).glob('*')))

print(f"Found {file_count} files")
