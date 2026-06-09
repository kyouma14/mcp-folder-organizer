import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP


project_root = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(project_root))

from core.organizer import organize_directory
from core.scanner import scan_dir
from core.undo import undo

mcp = FastMCP("folder-organizer")

@mcp.tool()
def organize_folder(path: str):

    """
    Scans a directory and returns information 
    about contained files. Also organizes the files

    """

    files = scan_dir(path)
    return organize_directory(files, path)

@mcp.tool()
def undo_organization(path: str):

    """
    Undoes the organization of files in a folder
    when they are organized according to their file extensions

    """
    return undo(path)


if __name__ == "__main__":
    mcp.run()



