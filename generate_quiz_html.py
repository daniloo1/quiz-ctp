import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "quiz_data.json"
HTML_PATH = BASE_DIR / "index.html"

with DATA_PATH.open(encoding="utf-8") as source:
    questions = json.load(source)

html = HTML_PATH.read_text(encoding="utf-8")
pattern = r"const rawQuestions = \[.*?\];"
replacement = "const rawQuestions = " + json.dumps(questions, ensure_ascii=False) + ";"
updated_html, replacements = re.subn(pattern, lambda _: replacement, html, count=1, flags=re.DOTALL)

if replacements != 1:
    raise SystemExit("Impossibile individuare l'array delle domande in index.html; nessun file è stato modificato.")

HTML_PATH.write_text(updated_html, encoding="utf-8")
print(f"index.html aggiornato con successo ({len(questions)} domande; interfaccia preservata).")
