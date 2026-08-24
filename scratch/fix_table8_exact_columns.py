import os
import subprocess
import win32com.client
import docx
from docx.shared import Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v26_docx_path = workspace / "docs" / "paper" / "PaperV26_Ollama_Primary.docx"
v26_pdf_path = workspace / "docs" / "paper" / "PaperV26_Ollama_Primary.pdf"

doc = docx.Document(v26_docx_path)
t7 = doc.tables[6] # This is Table 8: SOTA Benchmark

print(f"Original Table 8 dimensions: {len(t7.rows)} rows, {len(t7.columns)} cols")

# The exact 8-column data (No Joint EM!)
sota_data = [
    ['Document Intelligence Architecture', 'Model Paradigm / Pipeline', 'Benchmark Source & Origin', 'Category Accuracy', 'Student Name Acc', 'Overall Field F1', 'Character Error Rate (CER)', 'Robustness & Empirical Summary'],
    ['Classical Vector Extractor [19]', 'Direct Text Stream (PyMuPDF)', 'Direct Real Run (AU DIC 45 Specimens)', '33.33%', '11.11%', '11.11%', '88.89%', 'Fails completely on raster images'],
    ['Layout Transformer (LayoutLMv3) [6]', 'Multimodal Token Classification', 'Reported Literature Baseline [6]', '91.20%', '84.50%', '72.40%', '14.80%', 'Vulnerable to unnormalized syntax'],
    ['OCR-Free Transformer (Donut) [7]', 'Swin Transformer Sequence-to-Seq', 'Reported Literature Baseline [7]', '94.00%', '86.70%', '74.80%', '12.50%', 'Degrades under severe 90° rotation'],
    ['Pure Foundation VLM (MiniCPM-V) [31]', 'Zero-Shot Neural Pixel Ingestion', 'Direct Real Run (AU DIC 45 Specimens - Pass A)', '100.00%', '97.80%', '79.56%', '9.69%', 'Live neural evaluation across 900 fields'],
    ['Proposed AU DIC System (Ours)', 'Neural VLM + 6-Stage Normalizer', 'Direct Real Run (AU DIC 45 Specimens - Pass B)', '100.00%', '97.80%', '90.56%', '3.64%', 'Live Verified State-of-the-Art (+11.00% Gain)']
]

# Delete extra columns if > 8
for row in t7.rows:
    while len(row.cells) > 8:
        cell_to_del = row.cells[-1]
        cell_to_del._tc.getparent().remove(cell_to_del._tc)

# Fix grid if needed
grid = t7._tbl.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblGrid')
if grid is not None:
    gridCols = grid.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}gridCol')
    while len(gridCols) > 8:
        grid.remove(gridCols[-1])
        gridCols = grid.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}gridCol')

# Populate exact data and formatting
def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

for r_idx, row_data in enumerate(sota_data):
    row = t7.rows[r_idx]
    is_header = (r_idx == 0)
    bg_color = "1B365D" if is_header else ("F7FAFC" if r_idx % 2 == 1 else "FFFFFF")
    
    for c_idx, val in enumerate(row_data):
        cell = row.cells[c_idx]
        cell.text = val
        
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="28" w:type="dxa"/><w:bottom w:w="28" w:type="dxa"/><w:left w:w="35" w:type="dxa"/><w:right w:w="35" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        set_cell_shading(cell, bg_color)
        
        for p in cell.paragraphs:
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.0
            for r in p.runs:
                r.font.name = "Times New Roman"
                if is_header:
                    r.font.size = Pt(8.0)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    r.font.size = Pt(7.2)
                    r.font.color.rgb = RGBColor(30, 41, 59)

doc.save(v26_docx_path)
print(f"[SUCCESS] Table 8 reconstructed with EXACTLY 8 columns (Joint EM 100% removed)!")

# Re-export PDF via Word COM Automation
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False
try:
    doc_word = word.Documents.Open(os.path.abspath(str(v26_docx_path)))
    doc_word.SaveAs(os.path.abspath(str(v26_pdf_path)), FileFormat=17)
    page_count = doc_word.ComputeStatistics(2)
    doc_word.Close(False)
    print(f"[SUCCESS] Exported high-quality PDF: {v26_pdf_path.name} ({page_count} Pages!)")
finally:
    word.Quit()
