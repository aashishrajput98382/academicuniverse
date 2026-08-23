import os
from pathlib import Path

# 1. Create Paper_V19.md
with open('docs/paper/Paper_V18.md', 'r', encoding='utf-8') as f:
    text_v18 = f.read()

with open('docs/paper/Paper_V19.md', 'w', encoding='utf-8') as f:
    f.write(text_v18)

print('[SUCCESS] Created docs/paper/Paper_V19.md')

# 2. Create generate_paperv19_pipeline.py
with open('scratch/generate_paperv18_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('PaperV18_Ollama_Primary.docx', 'PaperV19_Ollama_Primary.docx')
code = code.replace('PaperV18_Ollama_Primary.pdf', 'PaperV19_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V18', 'GENERATING PAPER V19')
code = code.replace('v18_docx_path', 'v19_docx_path')
code = code.replace('v18_pdf_path', 'v19_pdf_path')
code = code.replace('Saved clean PaperV18_Ollama_Primary.docx', 'Saved clean PaperV19_Ollama_Primary.docx')

# Point figure paths to mermaid-py generated images
code = code.replace('figure1_system_architecture.png', 'figure1_system_architecture_mermaid.png')
code = code.replace('figure2_option_b_pipeline.png', 'figure2_data_flow_mermaid.png')
code = code.replace('extracted_figures/image3.png', 'figure3_neural_pipeline_mermaid.png')

with open('scratch/generate_paperv19_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv19_pipeline.py')
