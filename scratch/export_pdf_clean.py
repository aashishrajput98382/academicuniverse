import os
import subprocess
import win32com.client
from pathlib import Path

# Kill any stale WINWORD.EXE
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

docx_path = os.path.abspath("docs/paper/PaperV23_Ollama_Primary.docx")
pdf_path = os.path.abspath("docs/paper/PaperV23_Ollama_Primary.pdf")

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False
try:
    doc = word.Documents.Open(docx_path)
    doc.ExportAsFixedFormat(pdf_path, 17) # 17 = wdExportFormatPDF
    pages = doc.ComputeStatistics(2)
    doc.Close(False)
    print(f"[SUCCESS] Exported high-quality PDF: PaperV23_Ollama_Primary.pdf ({pages} Pages!)")
finally:
    word.Quit()
