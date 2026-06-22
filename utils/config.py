
import os

FOLDERS = [
    "data",
    "logs",
    "exports"
]

for folder in FOLDERS:
    os.makedirs(folder,exist_ok=True)

