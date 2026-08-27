import os
import re
import subprocess
import win32com.client
import docx
import pypdf
from docx.shared import Pt, RGBColor
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v40_docx_path = workspace / "docs" / "paper" / "PaperV40_Ollama_Primary.docx"
v41_docx_path = workspace / "docs" / "paper" / "PaperV41_Ollama_Primary.docx"
v41_pdf_path  = workspace / "docs" / "paper" / "PaperV41_Ollama_Primary.pdf"

assert v40_docx_path.exists(), f"Error: {v40_docx_path} does not exist!"

print("=================================================================")
print(" GENERATING PAPER V41 (450-DOCUMENT FULL BENCHMARK DATASET UPDATE)")
print("=================================================================")

doc = docx.Document(v40_docx_path)

# 1. Paragraph Text Replacements
text_replacements = [
    ("45 physical multi-modal specimens", "450 synthetic multi-modal document specimens representing diverse optical capture conditions"),
    ("45 synthetic multi-modal document specimens", "450 synthetic multi-modal document specimens"),
    ("45 synthetic document specimens", "450 synthetic document specimens"),
    ("45 document specimens", "450 document specimens"),
    ("across 900 paired field observations", "across 9,000 paired field observations"),
    ("across 900 atomic field observations", "across 9,000 atomic field observations"),
    ("(900 paired field observations)", "(9,000 paired field observations)"),
    ("900 evaluated ground-truth field observations", "9,000 evaluated ground-truth field observations"),
    ("(45 Specimens / 900 Fields)", "(450 Specimens / 9,000 Fields)"),
    ("(N = 900,", "(N = 9,000,"),
    ("79.56% F1", "81.77% F1"),
    ("90.56% F1", "92.92% F1"),
    ("90.56% normalized field F1", "92.92% normalized field F1"),
    ("3.64% CER", "2.45% CER"),
    ("9.69% to 3.64%", "8.14% to 2.45%"),
    ("62.44% relative CER reduction", "69.90% relative CER reduction"),
    ("McNemar $\\chi^2 = 97.01, p < 0.0001$", "McNemar $\\chi^2 = 1,002.00, p < 10^{-200}$"),
    ("McNemar \\chi^2 = 97.01", "McNemar \\chi^2 = 1,002.00"),
    ("yielding $\\chi^2 = 97.01$", "yielding $\\chi^2 = 1,002.00$"),
    ("99 false-negative field mismatches", "1,004 false-negative field mismatches"),
    ("resolved 99 false-negative", "resolved 1,004 false-negative"),
    ("All 99 `FORMAT_ERROR`", "All 1,004 `FORMAT_ERROR`"),
    ("converted into 815 `EXACT_MATCH`", "converted into 8,363 `EXACT_MATCH`"),
    ("run_1785959173886", "run_450_live_gpu_1787773778444"),
    ("0bc63b0", "18745ce"),
    ("5 Vector PDFs", "50 Vector PDFs"),
    ("20 Lossless PNGs", "200 Lossless PNGs"),
    ("20 Compressed JPEGs", "200 Compressed JPEGs"),
]

for p in doc.paragraphs:
    orig_text = p.text
    new_text = orig_text
    for old_s, new_s in text_replacements:
        if old_s in new_text:
            new_text = new_text.replace(old_s, new_s)
    if new_text != orig_text:
        p.text = new_text
        for r in p.runs:
            r.font.name = "Times New Roman"

# 2. Table Cell Replacements
for tbl in doc.tables:
    for row in tbl.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                orig_t = p.text
                new_t = orig_t
                for old_s, new_s in text_replacements:
                    if old_s in new_t:
                        new_t = new_t.replace(old_s, new_s)
                # Specific Table Cell Updates
                if "97.01" in new_t: new_t = new_t.replace("97.01", "1002.00")
                if "79.56%" in new_t: new_t = new_t.replace("79.56%", "81.77%")
                if "90.56%" in new_t: new_t = new_t.replace("90.56%", "92.92%")
                if "9.69%" in new_t: new_t = new_t.replace("9.69%", "8.14%")
                if "3.64%" in new_t: new_t = new_t.replace("3.64%", "2.45%")
                if "11.00%" in new_t: new_t = new_t.replace("11.00%", "11.16%")
                if "-6.05%" in new_t: new_t = new_t.replace("-6.05%", "-5.69%")
                if "+13.83%" in new_t: new_t = new_t.replace("+13.83%", "+13.64%")
                if "-62.44%" in new_t: new_t = new_t.replace("-62.44%", "-69.90%")
                if "45 Physical Specimens" in new_t: new_t = new_t.replace("45 Physical Specimens", "450 Physical Specimens")
                if "45 Specimens" in new_t: new_t = new_t.replace("45 Specimens", "450 Specimens")
                if "900 Fields" in new_t: new_t = new_t.replace("900 Fields", "9,000 Fields")
                if "900 (100%)" in new_t: new_t = new_t.replace("900 (100%)", "9,000 (100%)")
                if "716 (79.56%)" in new_t: new_t = new_t.replace("716 (79.56%)", "7,359 (81.77%)")
                if "815 (90.56%)" in new_t: new_t = new_t.replace("815 (90.56%)", "8,363 (92.92%)")
                if "99 (11.00%)" in new_t: new_t = new_t.replace("99 (11.00%)", "1,004 (11.16%)")
                if "85 (9.44%)" in new_t: new_t = new_t.replace("85 (9.44%)", "637 (7.08%)")
                if "+99" in new_t: new_t = new_t.replace("+99", "+1,004")
                if "-99" in new_t: new_t = new_t.replace("-99", "-1,004")
                
                # Rule corrections counts (Table 10)
                if "Date Normalizer" in cell.text and "46" in new_t and "46.46%" in new_t:
                    new_t = new_t.replace("46", "462").replace("46.46%", "46.02%")
                if "Roll Number Normalizer" in cell.text and "30" in new_t and "30.30%" in new_t:
                    new_t = new_t.replace("30", "304").replace("30.30%", "30.28%")
                if "Numeric Normalizer" in cell.text and "23" in new_t and "23.23%" in new_t:
                    new_t = new_t.replace("23", "238").replace("23.23%", "23.70%")
                if "Total Corrected Mismatches" in cell.text and "99" in new_t:
                    new_t = new_t.replace("99", "1,004")
                    
                # Table 3 row counts
                if "16 Specimens (320 Fields)" in new_t: new_t = new_t.replace("16 Specimens (320 Fields)", "160 Specimens (3,200 Fields)")
                if "13 Specimens (260 Fields)" in new_t: new_t = new_t.replace("13 Specimens (260 Fields)", "130 Specimens (2,600 Fields)")
                if "45 Synthetic Document Specimens (900 Fields)" in new_t: new_t = new_t.replace("45 Synthetic Document Specimens (900 Fields)", "450 Synthetic Document Specimens (9,000 Fields)")
                if "2 PDFs" in new_t: new_t = new_t.replace("2 PDFs", "20 PDFs")
                if "1 PDF" in new_t: new_t = new_t.replace("1 PDF", "10 PDFs")
                if "7 PNGs" in new_t: new_t = new_t.replace("7 PNGs", "70 PNGs")
                if "6 PNGs" in new_t: new_t = new_t.replace("6 PNGs", "60 PNGs")
                if "7 JPEGs" in new_t: new_t = new_t.replace("7 JPEGs", "70 JPEGs")
                if "6 JPEGs" in new_t: new_t = new_t.replace("6 JPEGs", "60 JPEGs")
                
                # Table 7 counts
                if "15" == new_t.strip() and "clean" in row.cells[0].text: new_t = "150"
                if "10" == new_t.strip() and ("scanner_copy" in row.cells[0].text or "mobile_camera" in row.cells[0].text or "rotated_90" in row.cells[0].text): new_t = "100"
                if "45" == new_t.strip() and "Overall Total" in row.cells[0].text: new_t = "450"

                if new_t != orig_t:
                    p.text = new_t
                    for r in p.runs:
                        r.font.name = "Times New Roman"

# Save DOCX
doc.save(v41_docx_path)
print(f"[SUCCESS] Saved PaperV41_Ollama_Primary.docx!")

# Export to PDF via Word COM
print("[STEP] Exporting PaperV41_Ollama_Primary.pdf via Word COM...")
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False

try:
    doc_com = word.Documents.Open(str(v41_docx_path.resolve()))
    doc_com.SaveAs(str(v41_pdf_path.resolve()), FileFormat=17) # 17 = wdFormatPDF
    doc_com.Close(False)
    print(f"[SUCCESS] Exported PaperV41_Ollama_Primary.pdf!")
finally:
    word.Quit()
    subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

# Verify page count
reader = pypdf.PdfReader(str(v41_pdf_path))
pages = len(reader.pages)
print(f"\n[INFO] Paper V41 PDF Page Count: {pages} pages")
assert pages <= 20, f"Error: PDF exceeds 20 pages ({pages})!"
print(f"[PASS] V41 PDF strictly within page budget: {pages} <= 20 pages!")
