import os
from pathlib import Path

with open('scratch/execute_v13_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v13_frozen_block = '''assert v13_docx.exists(), "CRITICAL: Frozen PaperV13_Ollama_Primary.docx missing!"
assert v13_pdf.exists(), "CRITICAL: Frozen PaperV13_Ollama_Primary.pdf missing!"
assert v13_md.exists(), "CRITICAL: Frozen Paper_V13.md missing!"
print("[PASS] Frozen Paper V13 artifacts verified intact.")'''

code = code.replace('v13_docx = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.docx"',
'''v13_docx = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.docx"
v13_pdf = workspace / "docs" / "paper" / "PaperV13_Ollama_Primary.pdf"
v13_md = workspace / "docs" / "paper" / "Paper_V13.md"

v14_docx = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.docx"
v14_pdf = workspace / "docs" / "paper" / "PaperV14_Ollama_Primary.pdf"
v14_md = workspace / "docs" / "paper" / "Paper_V14.md"''')

code = code.replace('manifest_v13_path', 'manifest_v14_path')
code = code.replace('audit_v13_path', 'audit_v14_path')
code = code.replace('PAPER_V13_RELEASE_MANIFEST.md', 'PAPER_V14_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V13_CHANGE_AUDIT.md', 'PAPER_V14_CHANGE_AUDIT.md')
code = code.replace('PAPER V13', 'PAPER V14')
code = code.replace('Paper V13', 'Paper V14')
code = code.replace('V13', 'V14')
code = code.replace('v13_docx', 'v14_docx')
code = code.replace('v13_pdf', 'v14_pdf')
code = code.replace('v13_md', 'v14_md')

code = code.replace('print("[PASS] Frozen Paper V12 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V12 artifacts verified intact.")\n{v13_frozen_block}')

with open('scratch/execute_v14_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v14_verification_and_audit.py')
