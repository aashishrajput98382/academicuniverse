import os
from pathlib import Path

with open('scratch/generate_paperv12_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace V12 references with V13
code = code.replace('PaperV12_Ollama_Primary.docx', 'PaperV13_Ollama_Primary.docx')
code = code.replace('PaperV12_Ollama_Primary.pdf', 'PaperV13_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V12', 'GENERATING PAPER V13')
code = code.replace('v12_docx_path', 'v13_docx_path')
code = code.replace('v12_pdf_path', 'v13_pdf_path')
code = code.replace('Saved clean PaperV12_Ollama_Primary.docx', 'Saved clean PaperV13_Ollama_Primary.docx')

# Add Running Header setup
header_code = '''# 1. Clear incomplete/dummy footer text & Set Running Title Header
for s_idx, section in enumerate(doc.sections):
    footer = section.footer
    for p in footer.paragraphs:
        if "IEEE ACCESS" in p.text or "Page" in p.text:
            p.text = ""
    
    # Configure running title header (<= 60 letter spaces)
    section.different_first_page_header_footer = True
    header = section.header
    p_head = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    p_head.text = "Smart Academic Document Intelligence & Benchmarking"
    p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if p_head.runs:
        r_h = p_head.runs[0]
        r_h.font.name = "Times New Roman"
        r_h.font.size = Pt(8.5)
        r_h.font.italic = True
        r_h.font.color.rgb = RGBColor(0x60, 0x60, 0x60)'''

old_footer_block = '''# 1. Clear incomplete/dummy footer text
for s_idx, section in enumerate(doc.sections):
    footer = section.footer
    for p in footer.paragraphs:
        if "IEEE ACCESS" in p.text or "Page" in p.text:
            p.text = ""'''

code = code.replace(old_footer_block, header_code)

# Add Corresponding Author line to P1
corr_line = '''
# LINE BREAK 3 -> LINE 4 — CORRESPONDING AUTHOR NOTE
p1.add_run("\\n")
r_corr = p1.add_run("*Corresponding Author: Aashish Rajput (2023329421.aashish@ug.sharda.ac.in)")
r_corr.font.name = "Times New Roman"
r_corr.font.size = Pt(9.0)
r_corr.font.italic = True
'''

old_p1_end = 'p1.add_run(" 2023265132.avdesh@ug.sharda.ac.in").font.size = Pt(9.5)'
code = code.replace(old_p1_end, old_p1_end + corr_line)

with open('scratch/generate_paperv13_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv13_pipeline.py')
