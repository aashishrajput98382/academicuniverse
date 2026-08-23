import os
from pathlib import Path

with open('scratch/execute_v12_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add V12 to frozen check list, and set V13 as current
v12_frozen_block = '''assert v12_docx.exists(), "CRITICAL: Frozen PaperV12_Ollama_Primary.docx missing!"
assert v12_pdf.exists(), "CRITICAL: Frozen PaperV12_Ollama_Primary.pdf missing!"
assert v12_md.exists(), "CRITICAL: Frozen Paper_V12.md missing!"
print("[PASS] Frozen Paper V12 artifacts verified intact.")'''

code = code.replace('v12_docx = workspace / "docs" / "paper" / "PaperV12_Ollama_Primary.docx"',
'''v12_docx = workspace / "docs" / "paper" / "PaperV12_Ollama_Primary.docx"
v12_pdf = workspace / "docs" / "paper" / "PaperV12_Ollama_Primary.pdf"
v12_md = workspace / "docs" / "paper" / "Paper_V12.md"

v13_docx = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.docx"
v13_pdf = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.pdf"
v13_md = workspace / "docs" / "paper" / "Paper_V13.md"''')

code = code.replace('manifest_v12_path', 'manifest_v13_path')
code = code.replace('audit_v12_path', 'audit_v13_path')
code = code.replace('PAPER_V12_RELEASE_MANIFEST.md', 'PAPER_V13_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V12_CHANGE_AUDIT.md', 'PAPER_V13_CHANGE_AUDIT.md')
code = code.replace('PAPER V12', 'PAPER V13')
code = code.replace('Paper V12', 'Paper V13')
code = code.replace('V12', 'V13')
code = code.replace('v12_docx', 'v13_docx')
code = code.replace('v12_pdf', 'v13_pdf')
code = code.replace('v12_md', 'v13_md')

# Insert V12 frozen check
code = code.replace('print("[PASS] Frozen Paper V11 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V11 artifacts verified intact.")\n{v12_frozen_block}')

with open('scratch/execute_v13_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v13_verification_and_audit.py')
