from core.scanner import scan_dir
from core.organizer import organize_directory

file_path = "C:/Users/soham/Desktop/test"

files = scan_dir(file_path)


info = organize_directory(files, file_path)
print(info)
