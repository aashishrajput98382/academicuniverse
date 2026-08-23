import os
from pathlib import Path

# 1. Create Paper_V21.md
with open('docs/paper/Paper_V20.md', 'r', encoding='utf-8') as f:
    text_v20 = f.read()

with open('docs/paper/Paper_V21.md', 'w', encoding='utf-8') as f:
    f.write(text_v20)

print('[SUCCESS] Created docs/paper/Paper_V21.md')

# 2. Create generate_paperv21_pipeline.py
with open('scratch/generate_paperv20_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV20_Ollama_Primary.docx', 'PaperV21_Ollama_Primary.docx')
code = code.replace('PaperV20_Ollama_Primary.pdf', 'PaperV21_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V20', 'GENERATING PAPER V21')
code = code.replace('v20_docx_path', 'v21_docx_path')
code = code.replace('v20_pdf_path', 'v21_pdf_path')
code = code.replace('Saved clean PaperV20_Ollama_Primary.docx', 'Saved clean PaperV21_Ollama_Primary.docx')

with open('scratch/generate_paperv21_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv21_pipeline.py')
