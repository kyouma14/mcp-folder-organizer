from core.categorizer import categorize_file
from pathlib import Path
import shutil
import json

OPERATIONS_PATH = (
    Path(__file__).resolve().parent.parent / "storage" / "operations.json"
)



def move_file(source, destination_folder):
    destination_folder.mkdir(exist_ok = True)
    destination = destination_folder / source.name

    shutil.move(str(source), str(destination))



def organize_directory(files, base_directory):

    operations = []

    info = {
        "number_of_files" : len(files),
    }

    base_path = Path(base_directory)


    file_cnt = 0

    for file in files:
        category = categorize_file(file.extension)
        category_folder = base_path / category
        operations.append(
        {
            "operation_id" : str(file.path.parent),
            "from" : str(file.path),
            "to" : str(category_folder/file.name)
        }
        )

        move_file(file.path, category_folder)


        if(category in info):
            info[f"{category}"] = info[f"{category}"] + 1 
            file_cnt = file_cnt + 1 

        else:
            info[f"{category}"] = 1
            file_cnt = file_cnt + 1

    with open(
        OPERATIONS_PATH,
        "r"
    ) as f:
        operations_existing = json.load(f)

    operations_existing.extend(operations)

    OPERATIONS_PATH.write_text(
        json.dumps(operations_existing, indent=4)
    )

    if(info["number_of_files"] == file_cnt):
        info["status"] = "Success"

    else:
        info["status"] = "Failed"

    return info
    