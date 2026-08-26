import os
import re
import subprocess
import win32com.client
import docx
from docx.shared import Pt, RGBColor
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v38_docx_path = workspace / "docs" / "paper" / "PaperV38_Ollama_Primary.docx"
v39_docx_path = workspace / "docs" / "paper" / "PaperV39_Ollama_Primary.docx"
v39_pdf_path = workspace / "docs" / "paper" / "PaperV39_Ollama_Primary.pdf"

doc = docx.Document(v38_docx_path)

replacements = [
    ("yet benchmarking remains constrained by statutory privacy regulations (FERPA/GDPR) that prohibit sharing authentic student data.",
     "yet benchmarking remains constrained by privacy and data-protection requirements, including FERPA and GDPR, which impose significant restrictions on the disclosure and processing of identifiable educational records."),
    ("statutory privacy regulations—such as FERPA in the United States and GDPR in the European Union—strictly prohibit the public distribution of authentic student records containing personally identifiable information (PII) [17], [28], [35];",
     "privacy and data-protection frameworks—specifically FERPA in the United States and GDPR in the European Union—impose significant legal restrictions on the public disclosure, sharing, and processing of authentic student records containing personally identifiable information (PII) [17], [28], [35];"),
    ("First, statutory privacy frameworks—specifically FERPA in the United States and GDPR in the European Union—prohibit the public dissemination of authentic student records containing personally identifiable information [17], [28], [35], [48].",
     "First, statutory privacy and data-protection frameworks—specifically FERPA in the United States and GDPR in the European Union—impose strict regulatory constraints on the public dissemination and processing of authentic educational records containing student PII [17], [28], [35], [48]."),
    ("To address statutory privacy constraints (such as FERPA and GDPR) that prohibit the public dissemination of authentic student records containing personally identifiable information [17], [28], [35],",
     "To address statutory privacy and data-protection requirements (such as FERPA and GDPR) that impose substantial constraints on distributing identifiable educational records [17], [28], [35],"),
    ("Benchmarking document intelligence systems on academic credentials remains bottlenecked by statutory privacy regulations such as FERPA and GDPR,",
     "Benchmarking document intelligence systems on academic credentials remains bottlenecked by privacy and data-protection frameworks such as FERPA and GDPR that heavily restrict the sharing of authentic student records,")
]

for p in doc.paragraphs:
    for old_t, new_t in replacements:
        if old_t in p.text:
            p.text = p.text.replace(old_t, new_t)
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.0)
            print(f"[REPLACED PRIVACY TEXT] '{old_t[:40]}...' -> '{new_t[:40]}...'")

# Save DOCX
doc.save(v39_docx_path)
print(f"[SUCCESS] Saved PaperV39_Ollama_Primary.docx!")

# Export to PDF via Word COM
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False

try:
    doc_com = word.Documents.Open(str(v39_docx_path.resolve()))
    doc_com.SaveAs(str(v39_pdf_path.resolve()), FileFormat=17) # 17 = wdFormatPDF
    doc_com.Close(False)
    print(f"[SUCCESS] Exported PaperV39_Ollama_Primary.pdf!")
finally:
    word.Quit()
    subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)
