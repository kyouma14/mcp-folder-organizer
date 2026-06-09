from models.model import FileInfo
from pathlib import Path
from datetime import datetime 

def scan_dir(directory: str):
    files = []
    path = Path(directory)

    for file in path.rglob("*"):
        if file.is_file():
            info = FileInfo(
                path = file,
                name = file.name,
                extension = file.suffix.lower(),
                size = file.stat().st_size,
                modified_time= datetime.fromtimestamp(file.stat().st_mtime)
            )

            files.append(info)

    
    return files