import os
from pathlib import Path

with open('scratch/generate_paperv14_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV14_Ollama_Primary.docx', 'PaperV15_Ollama_Primary.docx')
code = code.replace('PaperV14_Ollama_Primary.pdf', 'PaperV15_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V14', 'GENERATING PAPER V15')
code = code.replace('v14_docx_path', 'v15_docx_path')
code = code.replace('v14_pdf_path', 'v15_pdf_path')
code = code.replace('Saved clean PaperV14_Ollama_Primary.docx', 'Saved clean PaperV15_Ollama_Primary.docx')

old_index_terms_code = '''exact_index_terms = (
    "Academic Document Intelligence, Document Extraction, Synthetic Benchmark Generation, "
    "Information Extraction, Semantic Normalization, OCR Error Analysis, Optical Degradation, Document Evaluation"
)'''

new_index_terms_code = '''exact_index_terms = (
    "Academic Document Intelligence, Synthetic Benchmark Generation, Document Information Extraction, "
    "Semantic Normalization, OCR Error Taxonomy, Vision-Language Models"
)'''

assert old_index_terms_code in code, "old_index_terms_code not found!"
code = code.replace(old_index_terms_code, new_index_terms_code)

with open('scratch/generate_paperv15_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv15_pipeline.py')
