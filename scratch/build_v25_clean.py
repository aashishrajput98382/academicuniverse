import re
from pathlib import Path

# Read V24 pipeline
with open('scratch/generate_paperv24_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace version strings
code = code.replace('PaperV24_Ollama_Primary.docx', 'PaperV25_Ollama_Primary.docx')
code = code.replace('PaperV24_Ollama_Primary.pdf', 'PaperV25_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V24', 'GENERATING PAPER V25 (ELEGANT LITERATURE & SOTA TABLES)')
code = code.replace('v24_docx_path', 'v25_docx_path')
code = code.replace('v24_pdf_path', 'v25_pdf_path')
code = code.replace('Saved clean PaperV24_Ollama_Primary.docx', 'Saved clean PaperV25_Ollama_Primary.docx')

with open('scratch/generate_paperv25_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Cleanly copied and updated scratch/generate_paperv25_pipeline.py!')
