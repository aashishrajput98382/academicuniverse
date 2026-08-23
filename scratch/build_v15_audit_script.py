import os
from pathlib import Path

with open('scratch/execute_v14_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v14_frozen_block = '''assert v14_docx.exists(), "CRITICAL: Frozen PaperV14_Ollama_Primary.docx missing!"
assert v14_pdf.exists(), "CRITICAL: Frozen PaperV14_Ollama_Primary.pdf missing!"
assert v14_md.exists(), "CRITICAL: Frozen Paper_V14.md missing!"
print("[PASS] Frozen Paper V14 artifacts verified intact.")'''

old_decl = '''v13_docx = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.docx"
v13_pdf = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.pdf"
v13_md = workspace / "docs" / "paper" / "Paper_V13.md"

v14_docx = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.docx"
v14_pdf = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.pdf"
v14_md = workspace / "docs" / "paper" / "Paper_V14.md"'''

new_decl = '''v13_docx = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.docx"
v13_pdf = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.pdf"
v13_md = workspace / "docs" / "paper" / "Paper_V13.md"

v14_docx = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.docx"
v14_pdf = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.pdf"
v14_md = workspace / "docs" / "paper" / "Paper_V14.md"

v15_docx = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.docx"
v15_pdf = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.pdf"
v15_md = workspace / "docs" / "paper" / "Paper_V15.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v14_path', 'manifest_v15_path')
code = code.replace('audit_v14_path', 'audit_v15_path')
code = code.replace('PAPER_V14_RELEASE_MANIFEST.md', 'PAPER_V15_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V14_CHANGE_AUDIT.md', 'PAPER_V15_CHANGE_AUDIT.md')
code = code.replace('PAPER V14', 'PAPER V15')
code = code.replace('Paper V14', 'Paper V15')
code = code.replace('V14', 'V15')
code = code.replace('v14_docx', 'v15_docx')
code = code.replace('v14_pdf', 'v15_pdf')
code = code.replace('v14_md', 'v15_md')

code = code.replace('print("[PASS] Frozen Paper V13 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V13 artifacts verified intact.")\n{v14_frozen_block}')

with open('scratch/execute_v15_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v15_verification_and_audit.py')
