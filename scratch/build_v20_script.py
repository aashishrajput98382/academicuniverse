import os
from pathlib import Path

# 1. Create Paper_V20.md
with open('docs/paper/Paper_V19.md', 'r', encoding='utf-8') as f:
    text_v19 = f.read()

with open('docs/paper/Paper_V20.md', 'w', encoding='utf-8') as f:
    f.write(text_v19)

print('[SUCCESS] Created docs/paper/Paper_V20.md')

# 2. Create generate_paperv20_pipeline.py
with open('scratch/generate_paperv19_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV19_Ollama_Primary.docx', 'PaperV20_Ollama_Primary.docx')
code = code.replace('PaperV19_Ollama_Primary.pdf', 'PaperV20_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V19', 'GENERATING PAPER V20')
code = code.replace('v19_docx_path', 'v20_docx_path')
code = code.replace('v19_pdf_path', 'v20_pdf_path')
code = code.replace('Saved clean PaperV19_Ollama_Primary.docx', 'Saved clean PaperV20_Ollama_Primary.docx')

with open('scratch/generate_paperv20_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv20_pipeline.py')
