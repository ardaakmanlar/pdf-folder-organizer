# pdf-folder-sorter

Organizes PDF files into folders based on numbers in their filenames.  

---

## 📘 About the Project

This script was developed during my internship at **FERNUS**, an educational technology company based in Ankara, Turkey.

It was created to automatically organize PDF files received from external publishing partners.  
These files were previously sorted manually, which was time-consuming and error-prone.  
With this tool, incoming documents can now be quickly grouped into folders like `BS-1`, `BS-2`, etc., based on the numbers in their filenames.


---

## 📦 What It Does

This script scans all `.pdf` files in a folder, extracts valid numbers (between 1 and 100) from filenames, and moves each file into a folder named after that number with a chosen base name (e.g., `BS-12`).

---

## 🚀 How to Use

1. Place the script in the folder where your `.pdf` files are.
2. Run the script in a terminal:
   
   **Step 1:** You'll be asked to enter the folder name prefix (e.g., `BS`).

   **Step 2:** The script will analyze the first PDF file and extract all valid numbers (between 1 and 100).

   **Step 3:** It will show you the numbers found in that file and ask you to pick which one to use (e.g., if it finds `[12, 34]`, you choose one).

   **Step 4:** All files will be sorted into folders based on that chosen number index.

---

---

## 🛠 Tech Stack

- **Python 3.10+**
- Built-in modules only:
  - `os` – for file system navigation
  - `shutil` – for moving files
  - `re` – for regex-based number extraction

✅ No external dependencies required.

---
