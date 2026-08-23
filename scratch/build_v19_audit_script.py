import os
from pathlib import Path

with open('scratch/execute_v18_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v18_frozen_block = '''assert v18_docx.exists(), "CRITICAL: Frozen PaperV18_Ollama_Primary.docx missing!"
assert v18_pdf.exists(), "CRITICAL: Frozen PaperV18_Ollama_Primary.pdf missing!"
assert v18_md.exists(), "CRITICAL: Frozen Paper_V18.md missing!"
print("[PASS] Frozen Paper V18 artifacts verified intact.")'''

old_decl = '''v17_docx = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.docx"
v17_pdf = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.pdf"
v17_md = workspace / "docs" / "paper" / "Paper_V17.md"

v18_docx = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.docx"
v18_pdf = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.pdf"
v18_md = workspace / "docs" / "paper" / "Paper_V18.md"'''

new_decl = '''v17_docx = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.docx"
v17_pdf = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.pdf"
v17_md = workspace / "docs" / "paper" / "Paper_V17.md"

v18_docx = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.docx"
v18_pdf = workspace / "docs" / "paper" / "PaperV18_Ollama_Primary.pdf"
v18_md = workspace / "docs" / "paper" / "Paper_V18.md"

v19_docx = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.docx"
v19_pdf = workspace / "docs" / "paper" / "PaperV19_Ollama_Primary.pdf"
v19_md = workspace / "docs" / "paper" / "Paper_V19.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v18_path', 'manifest_v19_path')
code = code.replace('audit_v18_path', 'audit_v19_path')
code = code.replace('PAPER_V18_RELEASE_MANIFEST.md', 'PAPER_V19_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V18_CHANGE_AUDIT.md', 'PAPER_V19_CHANGE_AUDIT.md')
code = code.replace('PAPER V18', 'PAPER V19')
code = code.replace('Paper V18', 'Paper V19')
code = code.replace('V18', 'V19')
code = code.replace('v18_docx', 'v19_docx')
code = code.replace('v18_pdf', 'v19_pdf')
code = code.replace('v18_md', 'v19_md')

code = code.replace('print("[PASS] Frozen Paper V17 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V17 artifacts verified intact.")\n{v18_frozen_block}')

with open('scratch/execute_v19_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v19_verification_and_audit.py')
