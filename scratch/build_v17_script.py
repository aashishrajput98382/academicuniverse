import os
from pathlib import Path

with open('scratch/generate_paperv16_pipeline.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Update paths
code = code.replace('PaperV16_Ollama_Primary.docx', 'PaperV17_Ollama_Primary.docx')
code = code.replace('PaperV16_Ollama_Primary.pdf', 'PaperV17_Ollama_Primary.pdf')
code = code.replace('GENERATING PAPER V16', 'GENERATING PAPER V17')
code = code.replace('v16_docx_path', 'v17_docx_path')
code = code.replace('v16_pdf_path', 'v17_pdf_path')
code = code.replace('Saved clean PaperV16_Ollama_Primary.docx', 'Saved clean PaperV17_Ollama_Primary.docx')

# List of table replacements in code
table_replaces = [
    ('TABLE XIV:', 'TABLE 14:'),
    ('TABLE XIII:', 'TABLE 13:'),
    ('TABLE XII:', 'TABLE 12:'),
    ('TABLE XI:', 'TABLE 11:'),
    ('TABLE X:', 'TABLE 10:'),
    ('TABLE IX:', 'TABLE 9:'),
    ('TABLE VIII:', 'TABLE 8:'),
    ('TABLE VII:', 'TABLE 7:'),
    ('TABLE VI:', 'TABLE 6:'),
    ('TABLE V:', 'TABLE 5:'),
    ('TABLE IV:', 'TABLE 4:'),
    ('TABLE III:', 'TABLE 3:'),
    ('TABLE II:', 'TABLE 2:'),
    ('TABLE I:', 'TABLE 1:'),
    ('Table XIV', 'Table 14'),
    ('Table XIII', 'Table 13'),
    ('Table XII', 'Table 12'),
    ('Table XI', 'Table 11'),
    ('Table X', 'Table 10'),
    ('Table IX', 'Table 9'),
    ('Table VIII', 'Table 8'),
    ('Table VII', 'Table 7'),
    ('Table VI', 'Table 6'),
    ('Table V', 'Table 5'),
    ('Table IV', 'Table 4'),
    ('Table III', 'Table 3'),
    ('Table II', 'Table 2'),
    ('Table I', 'Table 1'),
    ('Tables VII-XIV', 'Tables 7–14'),
    ('Tables VII–XIV', 'Tables 7–14'),
    ('Tables I–XIV', 'Tables 1–14'),
]

for r_str, a_str in table_replaces:
    code = code.replace(r_str, a_str)

with open('scratch/generate_paperv17_pipeline.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('[SUCCESS] Created scratch/generate_paperv17_pipeline.py')
