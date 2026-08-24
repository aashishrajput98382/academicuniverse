import docx
import re
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v32_docx_path = workspace / "docs" / "paper" / "PaperV32_Ollama_Primary.docx"
v32_md_path = workspace / "docs" / "paper" / "Paper_V32.md"

doc = docx.Document(v32_docx_path)
md_text = v32_md_path.read_text(encoding="utf-8")

print("=== AUDITING FOOTNOTES IN MARKDOWN & DOCX ===")

# Check markdown for footnote markers
md_footnotes = re.findall(r'\[\^(\w+)\]', md_text)
print(f"Markdown footnote markers [^N]: {md_footnotes}")

# Check docx paragraphs for footnotes or footnote references
docx_footnotes = []
for idx, p in enumerate(doc.paragraphs):
    # check for w:footnoteReference or superscript numbers
    fn_refs = p._element.xpath('.//w:footnoteReference')
    if fn_refs:
        docx_footnotes.append((idx, p.text))

print(f"Docx footnote references found: {len(docx_footnotes)}")

# Check table notes
table_notes = []
for idx, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if txt.startswith("*") or txt.startswith("†") or txt.startswith("Note:"):
        table_notes.append((idx, txt))

print(f"Table/Prose Asterisk Notes: {len(table_notes)}")
for tn in table_notes:
    print(f"  - {tn}")
