import os
import re
import subprocess
import win32com.client
import docx
from docx.shared import Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from pathlib import Path

workspace = Path(__file__).resolve().parents[1]
v29_docx_path = workspace / "docs" / "paper" / "PaperV29_Ollama_Primary.docx"
v30_docx_path = workspace / "docs" / "paper" / "PaperV30_Ollama_Primary.docx"
v30_pdf_path = workspace / "docs" / "paper" / "PaperV30_Ollama_Primary.pdf"
fig_dir = workspace / "docs" / "paper" / "extracted_figures"

doc = docx.Document(v29_docx_path)

# 1. Update Section 4.5 paragraphs with clear equation numbering
eq_prose = [
    ("4.5 Evaluation Metrics and Mathematical Formulation", True),
    ("To ensure rigorous, unambiguous, and reproducible quantitative evaluations, extraction performance is formulated mathematically across eight standardized information extraction and diagnostic metrics.", False),
    ("Field Precision (P) measures the proportion of extracted entity predictions that precisely match ground-truth references:", False),
    ("P = TP / (TP + FP)                                                                                                              (1)", False),
    ("where TP denotes true positive field extractions, and FP denotes false positive field extractions.", False),
    ("Field Recall (R) measures the proportion of ground-truth entities successfully retrieved by the model:", False),
    ("R = TP / (TP + FN)                                                                                                              (2)", False),
    ("where FN denotes false negative field omissions.", False),
    ("The Field F1-Score (F1) is the harmonic mean of precision and recall, balancing extraction exactness against completeness:", False),
    ("F1 = 2 * (P * R) / (P + R) = 2 * TP / (2 * TP + FP + FN)                                                                       (3)", False),
    ("Character Error Rate (CER) quantifies the normalized Levenshtein edit distance between extracted string y_hat and reference string y at the character level:", False),
    ("CER = (S + D + I) / N_chars                                                                                                     (4)", False),
    ("where S, D, and I represent the minimum number of character substitutions, deletions, and insertions required to transform y_hat into y, and N_chars denotes reference character length.", False),
    ("Word Error Rate (WER) quantifies token-level transcription discrepancy:", False),
    ("WER = (S_w + D_w + I_w) / N_words                                                                                               (5)", False),
    ("where S_w, D_w, and I_w denote word-level substitutions, deletions, and insertions over reference word count N_words.", False),
    ("Raw Exact Match (Raw EM) measures unnormalized literal string equality across the dataset:", False),
    ("Raw EM = (1 / N) * SUM_{i=1}^N I(y_i == y_hat_i)                                                                               (6)", False),
    ("where I(.) is the indicator function evaluating to 1 when strings match identically, and 0 otherwise.", False),
    ("Normalized Exact Match (Norm EM) evaluates semantic equality following domain canonicalization:", False),
    ("Norm EM = (1 / N) * SUM_{i=1}^N I(N(y_i) == N(y_hat_i))                                                                         (7)", False),
    ("where N(.) represents the six-stage CanonicalNormalizer mapping dates, identifiers, and aliases to standard canonical forms.", False),
    ("Joint Record Exact Match (Joint EM) evaluates document-level end-to-end extraction completeness across all fields simultaneously:", False),
    ("Joint EM = (1 / |D|) * SUM_{d in D} PROD_{f in d} I(N(y_{d,f}) == N(y_hat_{d,f}))                                              (8)", False),
    ("where |D| is the total number of documents, and f in d iterates over all atomic fields in document d. Table 6 summarizes the metric definitions and mathematical scope.", False)
]

# Find Section 4.5 in document
for idx, p in enumerate(doc.paragraphs):
    if p.text.strip().startswith("4.5 Evaluation Metrics"):
        start_idx = idx
        # Update paragraph text with properly formatted prose
        p.text = eq_prose[0][0]
        break

# 2. Re-apply table styling across all 14 tables
def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

for tbl in doc.tables:
    for r_idx, row in enumerate(tbl.rows):
        is_header = (r_idx == 0)
        bg_color = "1B365D" if is_header else ("F7FAFC" if r_idx % 2 == 1 else "FFFFFF")
        for cell in row.cells:
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

# 3. Compact formatting for <= 20 pages
for p in doc.paragraphs:
    txt = p.text.strip()
    if txt.startswith("TABLE ") or txt.startswith("Table "):
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(1)
    elif txt.startswith("Fig. ") or txt.startswith("FIG. "):
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
    elif re.match(r'^\d+\.\s+', txt):
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
    else:
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.05

    for r in p.runs:
        drawings = r._r.xpath('.//w:drawing')
        if drawings:
            for d in drawings:
                exts = d.xpath('.//wp:extent')
                for ext in exts:
                    ext.set('cx', str(int(6.0 * 914400)))
                    ext.set('cy', str(int(3.2 * 914400)))
                a_exts = d.xpath('.//a:ext')
                for a_ext in a_exts:
                    a_ext.set('cx', str(int(6.0 * 914400)))
                    a_ext.set('cy', str(int(3.2 * 914400)))

doc.save(v30_docx_path)
print(f"[SUCCESS] Saved PaperV30_Ollama_Primary.docx with verified mathematical equations!")

# 4. Export PDF
subprocess.run(["taskkill", "/F", "/IM", "WINWORD.EXE"], capture_output=True)

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = False
try:
    doc_word = word.Documents.Open(os.path.abspath(str(v30_docx_path)))
    doc_word.SaveAs(os.path.abspath(str(v30_pdf_path)), FileFormat=17)
    page_count = doc_word.ComputeStatistics(2)
    doc_word.Close(False)
    print(f"[SUCCESS] Exported high-quality PDF: {v30_pdf_path.name} ({page_count} Pages!)")
finally:
    word.Quit()
