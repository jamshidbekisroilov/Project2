gitignore_content = """
__pycache__/
*.pyc
.env
*.sqlite3
*.pdf
static/uploads/
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content.strip())

print(".gitignore fayli yaratildi va yozildi ✅")