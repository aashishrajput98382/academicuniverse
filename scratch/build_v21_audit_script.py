import os
from pathlib import Path

with open('scratch/execute_v20_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v20_frozen_block = '''assert v20_docx.exists(), "CRITICAL: Frozen PaperV20_Ollama_Primary.docx missing!"
assert v20_pdf.exists(), "CRITICAL: Frozen PaperV20_Ollama_Primary.pdf missing!"
assert v20_md.exists(), "CRITICAL: Frozen Paper_V20.md missing!"
print("[PASS] Frozen Paper V20 artifacts verified intact.")'''

old_decl = '''v19_docx = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.docx"
v19_pdf = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.pdf"
v19_md = workspace / "docs" / "paper" / "Paper_V19.md"

v20_docx = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.docx"
v20_pdf = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.pdf"
v20_md = workspace / "docs" / "paper" / "Paper_V20.md"'''

new_decl = '''v19_docx = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.docx"
v19_pdf = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.pdf"
v19_md = workspace / "docs" / "paper" / "Paper_V19.md"

v20_docx = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.docx"
v20_pdf = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.pdf"
v20_md = workspace / "docs" / "paper" / "Paper_V20.md"

v21_docx = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.docx"
v21_pdf = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.pdf"
v21_md = workspace / "docs" / "paper" / "Paper_V21.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v20_path', 'manifest_v21_path')
code = code.replace('audit_v20_path', 'audit_v21_path')
code = code.replace('PAPER_V20_RELEASE_MANIFEST.md', 'PAPER_V21_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V20_CHANGE_AUDIT.md', 'PAPER_V21_CHANGE_AUDIT.md')
code = code.replace('PAPER V20', 'PAPER V21')
code = code.replace('Paper V20', 'Paper V21')
code = code.replace('V20', 'V21')
code = code.replace('v20_docx', 'v21_docx')
code = code.replace('v20_pdf', 'v21_pdf')
code = code.replace('v20_md', 'v21_md')

code = code.replace('print("[PASS] Frozen Paper V19 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V19 artifacts verified intact.")\n{v20_frozen_block}')

with open('scratch/execute_v21_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v21_verification_and_audit.py')
