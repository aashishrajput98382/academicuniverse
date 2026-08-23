import os
from pathlib import Path

with open('scratch/execute_v15_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v15_frozen_block = '''assert v15_docx.exists(), "CRITICAL: Frozen PaperV15_Ollama_Primary.docx missing!"
assert v15_pdf.exists(), "CRITICAL: Frozen PaperV15_Ollama_Primary.pdf missing!"
assert v15_md.exists(), "CRITICAL: Frozen Paper_V15.md missing!"
print("[PASS] Frozen Paper V15 artifacts verified intact.")'''

old_decl = '''v14_docx = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.docx"
v14_pdf = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.pdf"
v14_md = workspace / "docs" / "paper" / "Paper_V14.md"

v15_docx = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.docx"
v15_pdf = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.pdf"
v15_md = workspace / "docs" / "paper" / "Paper_V15.md"'''

new_decl = '''v14_docx = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.docx"
v14_pdf = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.pdf"
v14_md = workspace / "docs" / "paper" / "Paper_V14.md"

v15_docx = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.docx"
v15_pdf = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.pdf"
v15_md = workspace / "docs" / "paper" / "Paper_V15.md"

v16_docx = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.docx"
v16_pdf = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.pdf"
v16_md = workspace / "docs" / "paper" / "Paper_V16.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v15_path', 'manifest_v16_path')
code = code.replace('audit_v15_path', 'audit_v16_path')
code = code.replace('PAPER_V15_RELEASE_MANIFEST.md', 'PAPER_V16_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V15_CHANGE_AUDIT.md', 'PAPER_V16_CHANGE_AUDIT.md')
code = code.replace('PAPER V15', 'PAPER V16')
code = code.replace('Paper V15', 'Paper V16')
code = code.replace('V15', 'V16')
code = code.replace('v15_docx', 'v16_docx')
code = code.replace('v15_pdf', 'v16_pdf')
code = code.replace('v15_md', 'v16_md')

code = code.replace('print("[PASS] Frozen Paper V14 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V14 artifacts verified intact.")\n{v15_frozen_block}')

# Update page count check to assert <= 20
page_check_old = 'assert len(pdf_reader.pages) == 22, f"Expected 22 pages, got {len(pdf_reader.pages)}"'
page_check_new = 'assert len(pdf_reader.pages) <= 20, f"Expected <= 20 pages, got {len(pdf_reader.pages)}"'
if page_check_old in code:
    code = code.replace(page_check_old, page_check_new)

with open('scratch/execute_v16_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v16_verification_and_audit.py')
