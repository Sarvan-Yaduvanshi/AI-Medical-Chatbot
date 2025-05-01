import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"  # Fixed space issue
]

# Loop through and create folders/files
for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != Path("."):  # Avoid creating '.' as a directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch()  # More idiomatic than open(..., "w").close()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
