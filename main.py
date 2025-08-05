import shutil
import os
import re

source_folder = input("Enter the source folder path: ").strip()
os.chdir(source_folder)

base_folder_name = input("Enter the base folder name (e.g., BS): ").strip()

pdf_files = [f for f in os.listdir() if f.lower().endswith(".pdf")]

selected_index = None

for pdf_file in pdf_files:
    matches = re.findall(r'(\d{1,10})', pdf_file)

    valid_numbers = [int(m) for m in matches if m.isdigit() and 1 <= int(m) <= 100]

    if not valid_numbers:
        print(f"⚠️ {pdf_file}: Geçerli sayı (1–100) bulunamadı.")
        continue

    if selected_index is None:
        print(f"İlk dosya: {pdf_file}")
        print(f"Bu dosyada bulunan geçerli numaralar: {valid_numbers}")
        while True:
            try:
                index = int(input(f"Hangisini kullanmak istersin? (1 ile {len(valid_numbers)} arasında): "))
                if 1 <= index <= len(valid_numbers):
                    selected_index = index - 1  
                    break
                else:
                    print("Geçersiz seçim, tekrar dene.")
            except ValueError:
                print("Lütfen bir sayı gir.")

    if selected_index < len(valid_numbers):
        hafta_numarasi = valid_numbers[selected_index]
        hedef_klasor = f"{base_folder_name}-{hafta_numarasi}"
        if not os.path.exists(hedef_klasor):
            os.makedirs(hedef_klasor)
        shutil.move(pdf_file, os.path.join(hedef_klasor, pdf_file))
        print(f"{pdf_file} → {hedef_klasor}")
    else:
        print(f"{pdf_file}: Seçilen index bu dosyada geçerli değil (bulunan: {valid_numbers})")
