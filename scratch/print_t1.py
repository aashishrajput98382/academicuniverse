import docx

doc = docx.Document('docs/paper/PaperV27_Ollama_Primary.docx')
t = doc.tables[0]
for i, r in enumerate(t.rows):
    print(f"Row {i}: {[c.text.strip().replace('\n', ' ') for c in r.cells]}")
