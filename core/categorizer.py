category_map = {
    "Images" : [".jpg", ".png", ".jpeg", ".gif"],
    "PDFs" : [".pdf"],
    "Videos" : [".mp4", ".mkv", ".avi"],
    "Archives" : [".zip", ".rar"],
    "Code" : [".py", ".cpp"],
    "Documents" : [".txt", ".docx"]
}

def categorize_file(extension: str):
    for category, extensions in category_map.items():
        if extension in extensions:
            return category
        
    return "Others"