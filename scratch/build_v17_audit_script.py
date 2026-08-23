import os
from pathlib import Path

with open('scratch/execute_v16_verification_and_audit.py', 'r', encoding='utf-8') as f:
    code = f.read()

v16_frozen_block = '''assert v16_docx.exists(), "CRITICAL: Frozen PaperV16_Ollama_Primary.docx missing!"
assert v16_pdf.exists(), "CRITICAL: Frozen PaperV16_Ollama_Primary.pdf missing!"
assert v16_md.exists(), "CRITICAL: Frozen Paper_V16.md missing!"
print("[PASS] Frozen Paper V16 artifacts verified intact.")'''

old_decl = '''v15_docx = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.docx"
v15_pdf = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.pdf"
v15_md = workspace / "docs" / "paper" / "Paper_V15.md"

v16_docx = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.docx"
v16_pdf = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.pdf"
v16_md = workspace / "docs" / "paper" / "Paper_V16.md"'''

new_decl = '''v15_docx = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.docx"
v15_pdf = workspace / "docs" / "paper" / "PaperV15_Ollama_Primary.pdf"
v15_md = workspace / "docs" / "paper" / "Paper_V15.md"

v16_docx = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.docx"
v16_pdf = workspace / "docs" / "paper" / "PaperV16_Ollama_Primary.pdf"
v16_md = workspace / "docs" / "paper" / "Paper_V16.md"

v17_docx = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.docx"
v17_pdf = workspace / "docs" / "paper" / "PaperV17_Ollama_Primary.pdf"
v17_md = workspace / "docs" / "paper" / "Paper_V17.md"'''

assert old_decl in code, "old_decl not found!"
code = code.replace(old_decl, new_decl)

code = code.replace('manifest_v16_path', 'manifest_v17_path')
code = code.replace('audit_v16_path', 'audit_v17_path')
code = code.replace('PAPER_V16_RELEASE_MANIFEST.md', 'PAPER_V17_RELEASE_MANIFEST.md')
code = code.replace('PAPER_V16_CHANGE_AUDIT.md', 'PAPER_V17_CHANGE_AUDIT.md')
code = code.replace('PAPER V16', 'PAPER V17')
code = code.replace('Paper V16', 'Paper V17')
code = code.replace('V16', 'V17')
code = code.replace('v16_docx', 'v17_docx')
code = code.replace('v16_pdf', 'v17_pdf')
code = code.replace('v16_md', 'v17_md')

code = code.replace('print("[PASS] Frozen Paper V15 artifacts verified intact.")',
f'print("[PASS] Frozen Paper V15 artifacts verified intact.")\n{v16_frozen_block}')

# Update table titles in Section 5 check
old_sec5_tables = '''table_titles_in_sec5 = [
    "TABLE VII: FRAMEWORK VERIFICATION METRICS",
    "TABLE VIII: LIVE MODEL EXTRACTION & CLASSIFICATION PERFORMANCE",
    "TABLE IX: EMPIRICAL METRIC IMPACT OF SEMANTIC CANONICAL NORMALIZATION",
    "TABLE X: MISMATCH CORRECTION CONTRIBUTION BY NORMALIZER RULE",
    "TABLE XI: STATISTICAL HYPOTHESIS TESTING SUMMARY",
    "TABLE XII: EMPIRICAL BENCHMARK METRICS WITH 95% BOOTSTRAP CONFIDENCE INTERVALS",
    "TABLE XIII: NINE-CLASS OCR ERROR TAXONOMY DISTRIBUTION BEFORE AND AFTER NORMALIZATION",
    "TABLE XIV: CLASSICAL MACHINE LEARNING BENCHMARK COMPARISON"
]'''

new_sec5_tables = '''table_titles_in_sec5 = [
    "TABLE 7: FRAMEWORK VERIFICATION METRICS",
    "TABLE 8: LIVE MODEL EXTRACTION & CLASSIFICATION PERFORMANCE",
    "TABLE 9: EMPIRICAL METRIC IMPACT OF SEMANTIC CANONICAL NORMALIZATION",
    "TABLE 10: MISMATCH CORRECTION CONTRIBUTION BY NORMALIZER RULE",
    "TABLE 11: STATISTICAL HYPOTHESIS TESTING SUMMARY",
    "TABLE 12: EMPIRICAL BENCHMARK METRICS WITH 95% BOOTSTRAP CONFIDENCE INTERVALS",
    "TABLE 13: NINE-CLASS OCR ERROR TAXONOMY DISTRIBUTION BEFORE AND AFTER NORMALIZATION",
    "TABLE 14: CLASSICAL MACHINE LEARNING BENCHMARK COMPARISON"
]'''

assert old_sec5_tables in code, "old_sec5_tables not found!"
code = code.replace(old_sec5_tables, new_sec5_tables)

with open('scratch/execute_v17_verification_and_audit.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/execute_v17_verification_and_audit.py')
