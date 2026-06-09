from pydantic import BaseModel
from pathlib import Path
from datetime import datetime

class FileInfo(BaseModel):
    path: Path
    name: str
    extension: str
    size: int
    modified_time: datetime
    