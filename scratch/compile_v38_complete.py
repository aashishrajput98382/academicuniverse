import os
import re
import subprocess
import win32com.client
import docx
from docx.shared import Pt, RGBColor
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v37_docx_path = workspace / "docs" / "paper" / "PaperV37_Ollama_Primary.docx"
v38_docx_path = workspace / "docs" / "paper" / "PaperV38_Ollama_Primary.docx"
v38_pdf_path = workspace / "docs" / "paper" / "PaperV38_Ollama_Primary.pdf"

doc = docx.Document(v37_docx_path)

# Paragraph level replacements for clear, precise terminology
replacements = [
    ("The benchmark suite comprises 45 unique physical multi-modal specimens", 
     "The benchmark suite comprises 45 synthetic multi-modal document specimens representing diverse optical capture conditions"),
    ("comprises 45 unique physical multi-modal academic credential specimens",
     "comprises 45 synthetic multi-modal academic credential specimens representing diverse physical and optical capture conditions"),
    ("across all 45 physical specimens", "across all 45 synthetic document specimens"),
    ("on the identical 45 physical multi-modal specimens", "on the identical 45 synthetic multi-modal document specimens"),
    ("across the 45 physical specimens", "across the 45 synthetic multi-modal document specimens"),
    ("All 45 multi-modal physical specimens", "All 45 synthetic multi-modal document specimens"),
    ("Live empirical evaluation across 45 physical multi-modal specimens", 
     "Live empirical evaluation across 45 synthetic multi-modal document specimens representing diverse optical capture conditions"),
    ("Physical optical scanner noise", "Optical scanner and sensor noise")
]

for p in doc.paragraphs:
    for old_t, new_t in replacements:
        if old_t in p.text:
            p.text = p.text.replace(old_t, new_t)
            # Re-apply font styling
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.0)
            print(f"[REPLACED PARAGRAPH] '{old_t[:40]}...' -> '{new_t[:40]}...'")

# Table level replacements
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for old_t, new_t in [
                ("45 Physical Specimens (6,526 Fields)", "45 Synthetic Specimens (900 Fields)"),
                ("45 Physical Specimens (900 Fields)", "45 Synthetic Specimens (900 Fields)"),
                ("45 Physical Specimens Suite", "45 Synthetic Multi-Modal Specimens Suite"),
                ("45 Physical Specimens (5 Vector PDFs", "45 Synthetic Specimens (5 Vector PDFs"),
                ("Physical optical scanner noise", "Optical scanner and sensor noise"),
                ("Direct Live Run (AU DIC 45 Specimens)", "Direct Live Run (AU DIC 45 Synthetic Specimens)"),
                ("Direct Live Run (AU DIC 45 Specimens - Pass A)", "Direct Live Run (AU DIC 45 Synthetic Specimens - Pass A)"),
                ("Direct Live Run (AU DIC 45 Specimens - Pass B)", "Direct Live Run (AU DIC 45 Synthetic Specimens - Pass B)")
            ]:
                if old_t in cell.text:
                    cell.text = cell.text.replace(old_t, new_t)
                    for cp in cell.paragraphs:
                        for cr in cp.runs:
                            cr.font.name = "Times New Roman"
                            cr.font.size = Pt(8.0)
                    print(f"[REPLACED TABLE CELL] '{old_t}' -> '{new_t}'")

# Save DOCX
doc.save(v38_docx_path)
print(f"[SUCCESS] Saved PaperV38_Ollama_Primary.docx!")

# Export to PDF via Word COM
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False

try:
    doc_com = word.Documents.Open(str(v38_docx_path.resolve()))
    doc_com.SaveAs(str(v38_pdf_path.resolve()), FileFormat=17) # 17 = wdFormatPDF
    doc_com.Close(False)
    print(f"[SUCCESS] Exported PaperV38_Ollama_Primary.pdf!")
finally:
    word.Quit()
    subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)
