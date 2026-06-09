# mcp-folder-organizer
Organize folders using natural language through Claude Desktop + MCP, with persistent history and undo support.

# MCP Smart Folder Organizer

Organize folders using natural language through Claude Desktop + MCP, with built-in operation history and undo support.

---

## Overview

MCP Folder Organizer is a local filesystem automation tool built using **Python** and the **Model Context Protocol (MCP)**.

It allows users to organize folders directly from Claude Desktop using natural language prompts.

Unlike traditional scripts, the project maintains an operation history and supports **safe rollback (undo)** of previous organization actions.

Example:

```text
User:
Organize C:/Users/Soham/Desktop/test

↓

Claude Desktop

↓

MCP Tool

↓

Files grouped by type
```

Undo later:

```text
User:
Undo organization for C:/Users/Soham/Desktop/test
```

---

## Features

* Organize files into folders based on file type
* Natural language interaction through Claude Desktop
* MCP tool integration using FastMCP
* Persistent operation tracking
* Undo organization for specific folders
* Automatic cleanup of empty generated folders
* Support for multiple organization sessions
* Local-first (no cloud dependency)

---

## Example

Before:

```text
test/
├── report.pdf
├── image.jpg
├── notes.pdf
```

After:

```text
test/
├── PDFs/
│   ├── report.pdf
│   └── notes.pdf
│
└── Images/
    └── image.jpg
```

Undo:

```text
test/
├── report.pdf
├── image.jpg
├── notes.pdf
```

---

## Architecture

```text
Claude Desktop
        │
        ▼
MCP Server (FastMCP)
        │
        ▼
Tool Layer
(organize / undo)
        │
        ▼
Core Logic
(scanner → categorizer → organizer)
        │
        ▼
Filesystem
```

---

## Project Structure

```text
mcp-smart-folder-organizer/
│
├── mcp_server/
│   └── server.py
│
├── core/
│   ├── scanner.py
│   ├── categorizer.py
│   ├── organizer.py
│   └── undo.py
│
├── storage/
│   └── .gitkeep
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/kyouma14/mcp-folder-organizer.git
cd mcp-smart-folder-organizer
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Claude Desktop MCP

Add the server to Claude Desktop configuration.

Example:

```json
{
  "mcpServers": {
    "folder-organizer": {
      "command": "D:/mcp-project/.venv/Scripts/python.exe",
      "args": [
        "D:/mcp-project/mcp_server/server.py"
      ]
    }
  }
}
```

Restart Claude Desktop.

---

## Usage

Organize:

```text
Organize C:/Users/.../Downloads
```

Organize multiple folders:

```text
Organize C:/Users/.../test_1 and C:/Users/.../Downloads/test_2
```

Undo:

```text
Undo organization for C:/Users/.../Downloads
```

---

## Operation Tracking

The project stores organization history to support undo.

Example structure:

```json
[
  {
    "operation_id": "C:/Users/Desktop/test",
    "from": "C:/Users/Desktop/test/a.pdf",
    "to": "C:/Users/Desktop/test/PDFs/a.pdf"
  }
]
```

History is local only.

---

## Tech Stack

* Python
* FastMCP
* Claude Desktop
* pathlib
* JSON
* shutil

---

## Challenges Solved

* Python module resolution inside MCP servers
* JSON serialization of filesystem paths
* Persistent operation history
* Multi-session undo support
* Safe filesystem rollback
* Empty folder cleanup

---

## Future Improvements

* Preview mode before organization
* Semantic file categorization using LLMs
* Duplicate detection
* Metadata-based organization
* Operation timeline/history UI
* Batch rollback

---

## License

MIT

---

Built for experimentation with MCP, tool calling, and local AI-powered workflows.

