import os
from pathlib import Path

with open('scratch/generate_paperv17_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV17_Ollama_Primary.docx', 'PaperV18_Ollama_Primary.docx')
code = code.replace('PaperV17_Ollama_Primary.pdf', 'PaperV18_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V17', 'GENERATING PAPER V18')
code = code.replace('v17_docx_path', 'v18_docx_path')
code = code.replace('v17_pdf_path', 'v18_pdf_path')
code = code.replace('Saved clean PaperV17_Ollama_Primary.docx', 'Saved clean PaperV18_Ollama_Primary.docx')

old_p_sec3 = '''The system architecture illustrated in Fig. 1 is organized into two strictly decoupled operational subsystems: (1) the Academic Document Benchmark Generator (ADBG v1.0), which fabricates synthetic student records from Typst vector templates and applies a 14-operator optical degradation pipeline across four standardized quality profiles, and (2) the AU DIC Evaluation Subsystem, which performs live zero-shot inference ingestion, multi-stage semantic canonical normalization, multi-metric evaluation, and nine-class structured error classification without mutating persistent datastores.'''

new_p_sec3 = '''The system architecture illustrated in Fig. 1 is organized into two strictly decoupled operational subsystems: (1) the Production Human-in-the-Loop Document Intelligence Subsystem, which automates multi-format document ingestion, neural category classification (98%+ confidence), zero-shot multimodal VLM extraction, six-stage semantic canonicalization, interactive human-in-the-loop review, and direct canonical database synchronization for multi-semester transcript generation and CGPA compilation, and (2) the Academic Document Benchmark Generator (ADBG v1.0) and Evaluation Subsystem, which fabricates 360 seed-deterministic synthetic student records from Typst vector templates, applies a 14-operator optical degradation matrix across four standardized quality profiles, and performs decoupled nine-class OCR error taxonomy diagnostics and rigorous statistical hypothesis verification without mutating persistent data stores.'''

if old_p_sec3 in code:
    code = code.replace(old_p_sec3, new_p_sec3)

with open('scratch/generate_paperv18_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv18_pipeline.py')
