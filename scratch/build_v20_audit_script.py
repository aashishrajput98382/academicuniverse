import os
from pathlib import Path

with open('scratch/execute_v19_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v19_frozen_block = '''assert v19_docx.exists(), "CRITICAL: Frozen PaperV19_Ollama_Primary.docx missing!"
assert v19_pdf.exists(), "CRITICAL: Frozen PaperV19_Ollama_Primary.pdf missing!"
assert v19_md.exists(), "CRITICAL: Frozen Paper_V19.md missing!"
print("[PASS] Frozen Paper V19 artifacts verified intact.")'''

old_decl = '''v18_docx = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.docx"
v18_pdf = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.pdf"
v18_md = workspace / "docs" / "paper" / "Paper_V18.md"

v19_docx = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.docx"
v19_pdf = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.pdf"
v19_md = workspace / "docs" / "paper" / "Paper_V19.md"'''

new_decl = '''v18_docx = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.docx"
v18_pdf = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.pdf"
v18_md = workspace / "docs" / "paper" / "Paper_V18.md"

v19_docx = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.docx"
v19_pdf = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.pdf"
v19_md = workspace / "docs" / "paper" / "Paper_V19.md"

v20_docx = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.docx"
v20_pdf = workspace / "docs" / "paper" / "PaperV20_Ollama_Primary.pdf"
v20_md = workspace / "docs" / "paper" / "Paper_V20.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v19_path', 'manifest_v20_path')
code = code.replace('audit_v19_path', 'audit_v20_path')
code = code.replace('PAPER_V19_RELEASE_MANIFEST.md', 'PAPER_V20_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V19_CHANGE_AUDIT.md', 'PAPER_V20_CHANGE_AUDIT.md')
code = code.replace('PAPER V19', 'PAPER V20')
code = code.replace('Paper V19', 'Paper V20')
code = code.replace('V19', 'V20')
code = code.replace('v19_docx', 'v20_docx')
code = code.replace('v19_pdf', 'v20_pdf')
code = code.replace('v19_md', 'v20_md')

code = code.replace('print("[PASS] Frozen Paper V18 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V18 artifacts verified intact.")\n{v19_frozen_block}')

with open('scratch/execute_v20_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v20_verification_and_audit.py')
