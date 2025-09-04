import os

# Ignor qilinadigan papka va fayl kengaytmalari
IGNORED_DIRS = {"__pycache__"}
IGNORED_EXTENSIONS = {".pyc", ".pyo", ".log", ".tmp"}

def save_clean_structure(root_dir, output_file="structure.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for foldername, subfolders, filenames in os.walk(root_dir):
            # Ignor qilinadigan papkani o'tkazib yubor
            if any(ignored in foldername for ignored in IGNORED_DIRS):
                continue

            level = foldername.replace(root_dir, "").count(os.sep)
            indent = "    " * level
            f.write(f"{indent}{os.path.basename(foldername)}/\n")

            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext in IGNORED_EXTENSIONS:
                    continue
                f.write(f"{indent}    {filename}\n")

    print(f"✅ '{output_file}' faylga '{root_dir}' struktura yozildi (filtrlangan).")

# Misol: D:\#portfolio\devhub
save_clean_structure("D:\\#portfolio\\devhub")