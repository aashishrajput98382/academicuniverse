import os
import docx
import win32com.client
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v22_docx_path = workspace / "docs" / "paper" / "PaperV22_Ollama_Primary.docx"
v22_pdf_path = workspace / "docs" / "paper" / "PaperV22_Ollama_Primary.pdf"
fig_dir = workspace / "docs" / "paper" / "extracted_figures"

doc = docx.Document(v22_docx_path)

replaced = 0
for r_id, rel in doc.part.rels.items():
    ref = rel.target_ref
    for img_name in ["image4.png", "image5.png", "image6.png", "image7.png", "image8.png", "image9.png"]:
        if img_name in ref:
            img_file = fig_dir / img_name
            if img_file.exists():
                with open(img_file, "rb") as f:
                    rel.target_part._blob = f.read()
                replaced += 1
                print(f"[REPLACED] {r_id} ({ref}) -> with fresh 45-specimen {img_name}")

doc.save(v22_docx_path)
print(f"[SUCCESS] Saved Word document with {replaced} updated figures!")

# Re-export high-quality PDF via Word COM Automation
word = None
try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc_word = word.Documents.Open(os.path.abspath(str(v22_docx_path)))
    doc_word.SaveAs(os.path.abspath(str(v22_pdf_path)), FileFormat=17)
    page_count = doc_word.ComputeStatistics(2)
    doc_word.Close()
    print(f"[SUCCESS] Exported high-quality PDF: {v22_pdf_path.name} ({page_count} Pages!)")
except Exception as e:
    print(f"Word COM PDF Export Error: {e}")
finally:
    if word:
        try: word.Quit()
        except: pass
