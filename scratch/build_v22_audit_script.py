import os
from pathlib import Path

# Read V21 verification script
with open('scratch/execute_v21_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace V21 with V22 references
code = code.replace('v21_docx = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.docx"\nv21_pdf = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.pdf"\nv21_md = workspace / "docs" / "paper" / "Paper_V21.md"',
                    'v21_docx = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.docx"\nv21_pdf = workspace / "docs" / "paper" / "PaperV21_Ollama_Primary.pdf"\nv21_md = workspace / "docs" / "paper" / "Paper_V21.md"\n\nv22_docx = workspace / "docs" / "paper" / "PaperV22_Ollama_Primary.docx"\nv22_pdf = workspace / "docs" / "paper" / "PaperV22_Ollama_Primary.pdf"\nv22_md = workspace / "docs" / "paper" / "Paper_V22.md"')

code = code.replace('manifest_v21_path = workspace / "docs" / "paper" / "PAPER_V21_RELEASE_MANIFEST.md"',
                    'manifest_v22_path = workspace / "docs" / "paper" / "PAPER_V22_RELEASE_MANIFEST.md"')
code = code.replace('audit_v21_path = workspace / "docs" / "paper" / "PAPER_V21_CHANGE_AUDIT.md"',
                    'audit_v22_path = workspace / "docs" / "paper" / "PAPER_V22_CHANGE_AUDIT.md"')

code = code.replace('PAPER V21', 'PAPER V22')
code = code.replace('Paper V21', 'Paper V22')
code = code.replace('PaperV21', 'PaperV22')
code = code.replace('manifest_v21_path', 'manifest_v22_path')
code = code.replace('audit_v21_path', 'audit_v22_path')
code = code.replace('Paper_V21', 'Paper_V22')
code = code.replace('v21_docx', 'v22_docx')
code = code.replace('v21_pdf', 'v22_pdf')
code = code.replace('v21_md', 'v22_md')

with open('scratch/execute_v22_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v22_verification_and_audit.py')
