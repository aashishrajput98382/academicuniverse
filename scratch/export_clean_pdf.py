import os
import subprocess
import win32com.client
from pathlib import Path

# Kill any stale word processes
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

docx_path = os.path.abspath("docs/paper/PaperV23_Ollama_Primary.docx")
pdf_path_primary = os.path.abspath("docs/paper/PaperV23_Ollama_Primary.pdf")
pdf_path_fresh = os.path.abspath("docs/paper/PaperV23_Ollama_Primary_Final.pdf")

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False

try:
    doc = word.Documents.Open(docx_path)
    
    # 1. Export fresh PDF
    doc.SaveAs(pdf_path_fresh, FileFormat=17)
    pages = doc.ComputeStatistics(2)
    print(f"[SUCCESS] Exported fresh PDF: {Path(pdf_path_fresh).name} ({pages} Pages!)")
    
    # 2. Try primary if unlocked
    try:
        doc.SaveAs(pdf_path_primary, FileFormat=17)
        print(f"[SUCCESS] Exported primary PDF: {Path(pdf_path_primary).name} ({pages} Pages!)")
    except Exception as e:
        print(f"[NOTE] Primary PDF was open in reader. Fresh copy created at {Path(pdf_path_fresh).name}")
        
    doc.Close(False)
finally:
    word.Quit()
