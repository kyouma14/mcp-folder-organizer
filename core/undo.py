from pathlib import Path
import json 
from core.organizer import move_file

def undo(path : str):

    folders_to_cleanup = set()

    status = {}
    OPERATIONS_PATH = (
        Path(__file__).resolve().parent.parent / "storage" / "operations.json"
    )

    if not OPERATIONS_PATH.exists():
        return {
            "status" : "nothing to undo"
        }
    
    with open(
        OPERATIONS_PATH,
        "r",
    ) as f:
        operations = json.load(f)

    for op in operations:
        if(path == op["operation_id"] ):
            try:
                move_file(Path(op["to"]), Path(op["from"]).parent)
                folders_to_cleanup.add(Path(op["to"]).parent)

            except Exception:
                status["status"] =  "failed" 
                status["code"] = "One or more file paths may have been modified"
                return status
    
    status ["status"] = "success"
    status ["code"] = "All files have been moved to their original paths"

    for folder in folders_to_cleanup:
        try:
            folder.rmdir()

        except OSError:
            pass

    
    operations = [op for op in operations if op["operation_id"]!= path]
    OPERATIONS_PATH.write_text(
        json.dumps(
            operations,
            indent=4
        )
    )

    return status