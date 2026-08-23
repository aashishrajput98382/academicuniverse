import os
from pathlib import Path

with open('scratch/execute_v17_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v17_frozen_block = '''assert v17_docx.exists(), "CRITICAL: Frozen PaperV17_Ollama_Primary.docx missing!"
assert v17_pdf.exists(), "CRITICAL: Frozen PaperV17_Ollama_Primary.pdf missing!"
assert v17_md.exists(), "CRITICAL: Frozen Paper_V17.md missing!"
print("[PASS] Frozen Paper V17 artifacts verified intact.")'''

old_decl = '''v16_docx = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.docx"
v16_pdf = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.pdf"
v16_md = workspace / "docs" / "paper" / "Paper_V16.md"

v17_docx = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.docx"
v17_pdf = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.pdf"
v17_md = workspace / "docs" / "paper" / "Paper_V17.md"'''

new_decl = '''v16_docx = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.docx"
v16_pdf = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.pdf"
v16_md = workspace / "docs" / "paper" / "Paper_V16.md"

v17_docx = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.docx"
v17_pdf = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.pdf"
v17_md = workspace / "docs" / "paper" / "Paper_V17.md"

v18_docx = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.docx"
v18_pdf = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.pdf"
v18_md = workspace / "docs" / "paper" / "Paper_V18.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v17_path', 'manifest_v18_path')
code = code.replace('audit_v17_path', 'audit_v18_path')
code = code.replace('PAPER_V17_RELEASE_MANIFEST.md', 'PAPER_V18_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V17_CHANGE_AUDIT.md', 'PAPER_V18_CHANGE_AUDIT.md')
code = code.replace('PAPER V17', 'PAPER V18')
code = code.replace('Paper V17', 'Paper V18')
code = code.replace('V17', 'V18')
code = code.replace('v17_docx', 'v18_docx')
code = code.replace('v17_pdf', 'v18_pdf')
code = code.replace('v17_md', 'v18_md')

code = code.replace('print("[PASS] Frozen Paper V16 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V16 artifacts verified intact.")\n{v17_frozen_block}')

with open('scratch/execute_v18_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v18_verification_and_audit.py')
