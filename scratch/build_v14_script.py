import os
from pathlib import Path

with open('scratch/generate_paperv13_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV13_Ollama_Primary.docx', 'PaperV14_Ollama_Primary.docx')
code = code.replace('PaperV13_Ollama_Primary.pdf', 'PaperV14_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V13', 'GENERATING PAPER V14')
code = code.replace('v13_docx_path', 'v14_docx_path')
code = code.replace('v13_pdf_path', 'v14_pdf_path')
code = code.replace('Saved clean PaperV13_Ollama_Primary.docx', 'Saved clean PaperV14_Ollama_Primary.docx')

new_abstract_code = '''exact_abstract_text = (
    "Academic document intelligence systems are increasingly deployed to extract semi-structured credentials "
    "from higher education records, yet benchmarking remains constrained by statutory privacy regulations "
    "(FERPA/GDPR) that prohibit sharing authentic student data. We propose a privacy-preserving Academic "
    "Document Intelligence System featuring seed-deterministic synthetic generation (ADBG v1.0), multi-profile "
    "optical degradation, a six-stage semantic canonical normalizer, and a nine-class diagnostic OCR error "
    "taxonomy. The benchmark dataset comprises 360 synthetic specimens across certificates, marksheets, and "
    "student identity cards evaluated across four optical quality profiles (clean, scanner copy, mobile capture, "
    "and 90° rotation). In canonical live evaluation using MiniCPM-V (7.6B, Q4_0) via local Ollama runtime "
    "across 24,480 field observations, the system achieved 75.23% field F1, 74.60% raw exact match, 82.18% "
    "normalized exact match, 8.21% character error rate, and 100.00% category classification accuracy. Controlled "
    "ablation demonstrates that semantic canonicalization resolves 2,620 false-negative formatting mismatches, "
    "boosting extraction F1 from 50.00% to 95.49% (+45.49% gain) and reducing CER from 38.13% to 3.65% with "
    "high statistical significance (McNemar \u03c7\u00b2 = 2618.00, p < 0.0001). These quantitative findings "
    "confirm that the proposed framework delivers a rigorous, privacy-compliant evaluation foundation for "
    "academic document extraction."
)'''

# Locate exact_abstract_text block in code
import re
code = re.sub(r'exact_abstract_text = \([\s\S]*?\n\)', new_abstract_code, code)

with open('scratch/generate_paperv14_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv14_pipeline.py')
