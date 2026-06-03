# Assignment 2: File System Interaction
**Aya Saghraoui**

## Project Description
This program interacts directly with the Linux file system layer via Python's 
standard OS abstraction libraries. It accepts a directory path as input, scans it, 
and extracts core metadata (size in bytes and POSIX file permissions) for every 
file found.

## Technical Report: OS Functions & Libraries Justification
To interact with the underlying operating system file management system, the 
following specific Python libraries and native functions were utilized:

1. `os.listdir(path)`:
   - **Why:** This function acts as a wrapper around the POSIX standard C library
     functions `opendir()` and `readdir()`. It issues a system call to the OS kernel
     requesting the directory stream to list all filename entries stored within the
     specified directory inode.

2. `os.stat(path)`:
   - **Why:** This is a direct interface to the native Linux `stat()` system call.
     Rather than parsing text outputs, it queries the file's inode metadata directly
     from the file system. It returns a structure containing critical attributes,
     including `st_size` (file size in bytes) and `st_mode` (file type and
     permission bits).

3. `stat.filemode()`:
   - **Why:** The raw `st_mode` mask returned by the OS kernel is integer-encoded.
     This utility decodes the permission bits into the traditional human-readable
     POSIX representation (e.g., `-rw-r--r--`), explicitly showing read, write,
     and execute capabilities for User, Group, and Others.

A screenshot of the final execution is included in the repository.

## How to Run the Program

**1. Run the script from your terminal (Killercoda / Google Colab / Linux environment):**
```bash
python3 file_analyzer.py
```

**2. Enter the directory path when prompted:** 