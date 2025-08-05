# pdf-folder-sorter

Organizes PDF files into folders based on numbers in their filenames.  

---

## 📦 What It Does

This script scans all `.pdf` files in a folder, extracts valid numbers (between 1 and 100) from filenames, and moves each file into a folder named after that number with a chosen base name (e.g., `BS-12`).

---

## 🚀 How to Use

1. Place the script in the folder where your `.pdf` files are.
2. Run the script in a terminal:
   
  Step 1: You'll be asked to enter the folder name prefix.

  Step 2: The script will analyze the first PDF file and extract all valid numbers (between 1 and 100).

  Step 3: It will show you the numbers found in that file and ask you to pick which one to use (e.g., if it finds [12, 34], you can choose one).
