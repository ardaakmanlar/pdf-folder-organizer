# pdf-folder-sorter

A Python script that organizes PDF files into folders based on numbers in their filenames.

---

## About the Project

This project was developed during my internship at **FERNUS**, an educational technology company based in Ankara, Turkey.

It was built to automate the organization of PDF files received from external publishing partners. These files were previously sorted manually, which was both time-consuming and prone to error.

The tool was specifically designed for internal use at FERNUS to help manage incoming PDFs more efficiently within the book production workflow.

---

## What It Does

The script scans all `.pdf` files in a folder, extracts valid numbers (between 1 and 100) from their filenames, and moves each file into a folder named using a base prefix and the extracted number (e.g., `BS-12`).

---

## How to Use

1. Place the script in the folder containing your `.pdf` files.
2. Run the script in a terminal.
3. Enter the base folder name prefix  when prompted.
4. The script will extract numbers from the first file and ask you to select which number to use.
5. All PDF files will be moved into folders based on the selected number index.

---

## Tech Stack

This script uses only Python's standard library:

- `os` – file system operations  
- `shutil` – file movement  
- `re` – regular expressions for number matching

No external dependencies are required.
