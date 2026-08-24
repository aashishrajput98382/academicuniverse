import os
import re
from pathlib import Path

# 1. Read generate_paperv21_pipeline.py
with open('scratch/generate_paperv21_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 2. Update version strings
code = code.replace('PaperV21_Ollama_Primary.docx', 'PaperV22_Ollama_Primary.docx')
code = code.replace('PaperV21_Ollama_Primary.pdf', 'PaperV22_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V21', 'GENERATING PAPER V22 (MULTI-MODAL VISION BENCHMARK INTEGRATED)')
code = code.replace('v21_docx_path', 'v22_docx_path')
code = code.replace('v21_pdf_path', 'v22_pdf_path')
code = code.replace('Saved clean PaperV21_Ollama_Primary.docx', 'Saved clean PaperV22_Ollama_Primary.docx')

# 3. Update Commit in code if present
code = code.replace('Commit: `88140d1`', 'Commit: `91b9cb6`')

with open('scratch/generate_paperv22_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv22_pipeline.py')
