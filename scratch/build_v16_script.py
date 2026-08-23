import os
from pathlib import Path

with open('scratch/generate_paperv15_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV15_Ollama_Primary.docx', 'PaperV16_Ollama_Primary.docx')
code = code.replace('PaperV15_Ollama_Primary.pdf', 'PaperV16_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V15', 'GENERATING PAPER V16')
code = code.replace('v15_docx_path', 'v16_docx_path')
code = code.replace('v15_pdf_path', 'v16_pdf_path')
code = code.replace('Saved clean PaperV15_Ollama_Primary.docx', 'Saved clean PaperV16_Ollama_Primary.docx')

# Remove front-matter block between section 7 comment and doc.save, and add compact IEEE reference styling
idx_front = code.find("# 7. Front-Matter Page Layout & Native TOC")
idx_save = code.find("doc.save(v16_docx_path)")

front_matter_replacement = """# -------------------------------------------------------------
# 7. Standard IEEE Research Article Layout & Compact References (<= 20 Pages)
# -------------------------------------------------------------
# Format reference list with standard 8.5pt font and compact spacing to strictly satisfy <= 20 page constraint
for p in doc.paragraphs:
    txt = p.text.strip()
    if re.match(r'^\\[\\d+\\]\\s+', txt):
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(8.5)
"""

code_v16 = code[:idx_front] + front_matter_replacement + "\n" + code[idx_save:]

with open('scratch/generate_paperv16_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code_v16)

print('[SUCCESS] Created scratch/generate_paperv16_pipeline.py')
