import os
import docx
import win32com.client
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches, RGBColor
from pathlib import Path

workspace = Path.cwd()
docx_path = workspace / "docs" / "paper" / "FIGURE_CAPTIONS_AND_SYMBOLS.docx"
pdf_path = workspace / "docs" / "paper" / "FIGURE_CAPTIONS_AND_SYMBOLS.pdf"

doc = docx.Document()

# Set standard 1 inch margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(4)
r_t = p_title.add_run("List of Figure Captions & Symbols (Nomenclature)")
r_t.font.name = "Times New Roman"
r_t.font.size = Pt(16)
r_t.bold = True

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_meta.paragraph_format.space_after = Pt(14)
r_m = p_meta.add_run("Smart Academic Document Intelligence System: Automated Extraction, Normalization, and Benchmark Generation\nAuthors: Kushagra Singh Bhadauria, Aashish Rajput, and Avdesh Kumar Sah")
r_m.font.name = "Times New Roman"
r_m.font.size = Pt(10)
r_m.font.italic = True

# Section 1: Figure Captions
h1 = doc.add_paragraph()
h1.paragraph_format.space_before = Pt(12)
h1.paragraph_format.space_after = Pt(6)
r_h1 = h1.add_run("1. List of Figure Captions (Separate Sheet for Typesetting)")
r_h1.font.name = "Times New Roman"
r_h1.font.size = Pt(12)
r_h1.bold = True

captions = [
    ("Fig. 1. ", "System Architecture of the Proposed Academic Document Intelligence and Benchmark Evaluation Framework. The architecture decomposes into two decoupled subsystems: (1) Academic Document Benchmark Generator (ADBG v1.0) for vector template compilation and multi-profile optical degradation, and (2) AU DIC Evaluation Subsystem for read-only neural inference ingestion, semantic canonical normalization, and nine-class OCR error taxonomy classification."),
    ("Fig. 2. ", "Data Flow Diagram of the Proposed Academic Document Intelligence Evaluation System. Traces the end-to-end multi-level transformation lifecycle across Level 0 (Context Level), Level 1 (Framework Execution Flow), and Level 2 (Diagnostic Error Classification & Evaluation Engine)."),
    ("Fig. 3. ", "Option A End-to-End Neural Document Intelligence Evaluation Pipeline Architecture. Demonstrates direct image pixel tensor ingestion via Ollama local runtime to MiniCPM-V (7.6B Q4_0) without external OCR pre-segmentation."),
    ("Fig. 4. ", "Accuracy Improvement after Semantic Canonical Normalization. Bar chart illustrating field-level accuracy and exact match gains across Certificate, Marksheet, and ID Card document categories before and after normalization."),
    ("Fig. 5. ", "Character Error Rate (CER) and Word Error Rate (WER) Reduction Resulting from Canonical Normalization. Visualizes the 90.42% relative reduction in Character Error Rate (from 38.13% to 3.65%) and 90.53% reduction in Word Error Rate (from 285.31% to 27.01%)."),
    ("Fig. 6. ", "Total False-Negative Field Mismatches Resolved by Each Individual Domain Normalizer Rule. Horizontal distribution of the 2,620 corrected errors across Date, Roll Number, Degree Alias, Numeric, Honorific/Whitespace, and University Alias normalizers."),
    ("Fig. 7. ", "Field-by-Field Accuracy Improvement Comparing Raw String Matching Against Canonical Normalization. Detailed multi-field breakdown comparing baseline unnormalized exact match rates against post-canonicalization accuracy."),
    ("Fig. 8. ", "Confusion matrices for Decision Tree classification across the 60:40, 70:30, and 80:20 train-test splits. Evaluates the predictability of document extraction failure modes using axis-aligned decision trees (93.69% accuracy, 95.91% F1, 0.8303 MCC)."),
    ("Fig. 9. ", "Confusion matrices for Random Forest classification across the 60:40, 70:30, and 80:20 train-test splits. Compares ensemble bagging classification across 24,480 observations against decision tree models.")
]

for label, desc in captions:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    r_l = p.add_run(label)
    r_l.font.name = "Times New Roman"
    r_l.font.size = Pt(10)
    r_l.bold = True
    r_d = p.add_run(desc)
    r_d.font.name = "Times New Roman"
    r_d.font.size = Pt(10)

# Section 2: List of Symbols (Nomenclature)
h2 = doc.add_paragraph()
h2.paragraph_format.space_before = Pt(16)
h2.paragraph_format.space_after = Pt(6)
r_h2 = h2.add_run("2. List of Mathematical Symbols & Notations (Nomenclature)")
r_h2.font.name = "Times New Roman"
r_h2.font.size = Pt(12)
r_h2.bold = True

symbols_data = [
    ["Symbol", "Mathematical / Technical Meaning", "Unit / Domain"],
    ["P", "Field-level entity Precision (P = TP / (TP + FP))", "Ratio [0, 1]"],
    ["R", "Field-level entity Recall (R = TP / (TP + FN))", "Ratio [0, 1]"],
    ["F1", "Harmonic mean of Precision and Recall", "Percentage [0, 100%]"],
    ["CER", "Character Error Rate ((S + D + I) / N_chars via Levenshtein distance)", "Percentage [0, 100%]"],
    ["WER", "Word Error Rate ((Sw + Dw + Iw) / N_words)", "Percentage [0, inf)"],
    ["Raw EM", "Raw Exact Match rate (unnormalized string equality)", "Percentage [0, 100%]"],
    ["Norm EM", "Normalized Exact Match rate (post-canonicalization string equality)", "Percentage [0, 100%]"],
    ["Joint EM", "Document-level Joint Record Exact Match", "Percentage [0, 100%]"],
    ["N(.)", "Six-stage semantic canonicalization operator", "Transformation Function"],
    ["I(.)", "Indicator function (1 if condition holds, 0 otherwise)", "Binary {0, 1}"],
    ["TP, FP, FN", "True Positive, False Positive, and False Negative counts", "Integer >= 0"],
    ["S, D, I", "Substitutions, Deletions, and Insertions in character edit distance", "Integer >= 0"],
    ["chi^2", "McNemar's chi-squared test statistic for paired binary proportions", "Statistical Statistic"],
    ["W", "Wilcoxon signed-rank test statistic for paired non-parametric differences", "Statistical Statistic"],
    ["t", "Paired Student's t-test statistic", "Statistical Statistic"],
    ["p", "Statistical significance probability (p-value)", "Probability [0, 1]"],
    ["alpha", "Hypothesis rejection significance threshold (alpha = 0.01 or 0.05)", "Significance Level"],
    ["B", "Number of non-parametric bootstrap resampling iterations (B = 10,000)", "Integer Count"],
    ["N", "Total evaluated field observations (N = 24,480)", "Integer Count"],
    ["|D|", "Total evaluated document specimens (|D| = 360)", "Integer Count"]
]

tbl = doc.add_table(rows=len(symbols_data), cols=3)
tbl.style = 'Table Grid'
for r_idx, row in enumerate(symbols_data):
    for c_idx, val in enumerate(row):
        cell = tbl.cell(r_idx, c_idx)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(val)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        if r_idx == 0:
            r.bold = True

doc.save(docx_path)
print(f"[SUCCESS] Saved {docx_path.name}")

# Export PDF
word = None
try:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc_word = word.Documents.Open(os.path.abspath(str(docx_path)))
    doc_word.SaveAs(os.path.abspath(str(pdf_path)), FileFormat=17)
    doc_word.Close()
    print(f"[SUCCESS] Exported {pdf_path.name}")
except Exception as e:
    print(f"Export Error: {e}")
finally:
    if word:
        try: word.Quit()
        except: pass
